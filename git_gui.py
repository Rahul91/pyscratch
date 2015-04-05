#!/usr/bin/python2.7

import sys
import string
import base64
from Tkinter import Tk
from tkFileDialog import askopenfilename
from githubpy import github
from bs4 import BeautifulSoup
import urllib2

print "For using this app, you need to have Github auth token, please go through the link for more details:\nhttps://help.github.com/articles/creating-an-access-token-for-command-line-use/#creating-a-token\n\nAfter getting your token, just paste in here"
token = raw_input("Enter/paste your token : ")
print "Now, that you have your auth token, from next execution simply comment out first 3 lines of code and paste your token in program itself, save and enjoy"

#token = '33aa8aec26d79b1843d50385cdea04093b90570f'  #Github auth token for authorisation

def gitgui():
	gh = github.GitHub(access_token=token)
	username = str(gh.user.get()['login'])

	root = Tk()
	root.withdraw()
	root.filename = askopenfilename()
	filename = str(root.filename)
	filename_rev = filename[::-1]


	str_file =''
	for i in range(30):
		if filename_rev[i] == "/":
			break
		else:
			str_file = str_file + filename_rev[i]

	file_name = str_file[::-1]
	commit_message = raw_input("Enter your commit Message : ")


	with open(filename) as f:
		file_content = f.read()


	flag1 = 1
	j = 0

	list = gh.user.repos.get()

	while (j<=3):

		repo_name = raw_input("Enter the repo, you want your code to be pushed: ")
		for dictionary in list:
			if str(repo_name) != str(dictionary['name']):
				flag1 = 0
				
			else:
				flag1 = 1
				j = 5
				print "got a hit"
				break

		if flag1 == 0:
			print "I think, you have forgotten your repo names, have a look here, and try again."
			for dictionary in list:
				print dictionary['name']
			j += 1

		if j == 3:
			print "Tumse naa ho payega, Aborting"
			sys.exit(1)
			break



	link = "https://github.com/" + username + "/" + str(repo_name)
	url = urllib2.urlopen(link) 
	soup = BeautifulSoup(url)

	con = soup.find_all("a",{"class" : "js-directory-link"})
	count = len(con)

	flag2 = 0

	for title in con:
		if str(file_name) == str(title.text):
			flag2 = 1
			print "You are trying to push a file, which is already there on your remote. This feature is not in this module. Please try later and push a file which is not alrady pushed. Aborting."
			break


	if (flag1==1 and flag2==0):
		encoded_file =  base64.b64encode(file_content)
		gh = github.GitHub(access_token=token)
		username = str(gh.user.get()['login'])
		gh.repos(username)(repo_name)('contents')(file_name).put(path=file_content,message=commit_message,content=encoded_file)
		print ("File %s with commit message : %s pushed into your repo : %s" %(file_name, commit_message, repo_name))
		raw_input("Press Enter to exit :)")


if __name__ == "__main__":
	gitgui()