import os
import praw
import re
import sys
import requests 
import urllib
import urllib2
from subprocess import call
import wget
import time



reddit = praw.Reddit(client_id = '**********',
				     client_secret = '**********',
				     user_agent = '**********',
				     username = '**********',
				     password = '**********' 
				     )

print (reddit.read_only) 

# p = 0

# subr = str(input())

subr = 'wholesomememes'

pkp =  os.getcwd()

print pkp
if not os.path.exists(subr):
    os.makedirs(subr)


folderpath = str(pkp) +'/'+ subr +'/'
# print folderpath
os.chdir(folderpath) 



i = 1
pkp = list()
for submission in reddit.subreddit(subr).hot(limit=150):

	url2 = submission.url
	if '/i.' in url2:
		f = urllib2.urlopen(url2)
		# print type(f)
		f2 = str(url2)
		extention = f2.split(".")
		fname = str(i)+"."+extention[-1]
		with open(fname,"wb") as img:
			img.write(f.read())
		i+=1
		print url2
		print i,"^---"
	# fn = wget.download(url2)
	# print fn

	# if '/i.' in url:
	# 	# result = urllib.urlretrieve(url,'/media/sharma/X/')
	# 	pkp = url
	# 	print pkp
	# 	mm = str(i)
 # 		f = urllib.urlopen(pkp)
	# 	# wget.download(pkp)
	# 	data = f.read()
	# 	mm = str(i)
	# 	kk = mm+".jpeg"
	# 	with open(kk,"wb") as imf:
	# 		imf.write(data)
	# 	print("\n saved ",i)
	# 	time.sleep(1)
	# 	print ("\n")
	# 	i+=1
	# 	if(i==10):
	# 		exit(0)
	# 	# print filename
		
		
