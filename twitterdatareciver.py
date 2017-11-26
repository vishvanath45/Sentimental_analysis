#-*- coding: utf-8 -*-

from twython import Twython
from collections import Counter
import re
from sets import Set
import os, random
import sys
import pprint
from textblob import TextBlob
import time

#  test for regular expression
# mega_pkp = "One of our camera engineers @yolo #mega #lucky shares his top picks for cameras that are perfect for traveling light and making incred… https://t.co/iJTBa10JoQ"

# mega_pkp =  ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", mega_pkp).split())

# print mega_pkp

# def upload_random_image():
# 	local_folder_path = '/media/sharma/X/IMG Scraper/Reddit image downloader/wholesomememes/'
# 	address = random.choice(os.listdir(local_folder_path))
# 	# print address
# 	# address has something like 5.png
# 	final_add = local_folder_path+'/'+str(address)

# 	photo = open(final_add,'rb')

# 	response = twitter.upload_media(media=photo)
# 	twitter.update_status(status='i just uploded a random image through Twython, Amazing!', media_ids=[response['media_id']])


reload(sys)  # Reload is a hack
sys.setdefaultencoding('UTF8')

clean_html = re.compile('<.*?>')
consumer_key = '*****************'
consumer_secret = '*****************'
access_token = '*****************'
access_token_secret = '*****************'

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
times = 0
my_set = set()
while(times<1):

	print "sleeping ^-^ "
	time.sleep(5)
	print "just woke up (0_0)"

	msp = twitter.get_home_timeline(count=300,exclude_replies=True,include_rts=False)

	for kk in msp:
		# pprint.pprint(kk)
		# print "\n\n-------\n\n"
		user_screen_name = kk['user']['screen_name']
		if user_screen_name not in my_set:
			Tweet_text = str(kk['text'])
			Tweet_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", Tweet_text).split())
			
			analysis = TextBlob(Tweet_text)
			# senti: Neutral = 0, posit = +1, neg =-1
			senti = 0 

			if analysis.sentiment.polarity > 0:
				senti = 1
			elif(analysis.sentiment.polarity == 0):
				senti = 0
			else:
				senti = -1


			idd =  int(kk['id'])
			print idd
			print user_screen_name


			local_folder_path = './wholesomememes/'
			address = random.choice(os.listdir(local_folder_path))
			# print address
			# address has something like 5.png
			final_add = local_folder_path+'/'+str(address)

			photo = open(final_add,'rb')

			

			if(senti == -1):
				message = "Hi @%s, you seem to have a dull day, let me cheer you up with a wholesome meme!\nI am a bot 🤖, did i just break, reply 2 @vishva_nath " %(user_screen_name)
			elif(senti == 0):
				message = "Hi @%s, my sentimental senses have judged ur tweet as neutral, let me cheer you up!, have a wholesome meme, :D,\nI am a bot 🤖, did i just break?, reply 2 @vishva_nath " %(user_screen_name)
			else:
				message = "Hi @%s, you seem happy today! let me add to your happiness, have a wholesome meme! :D \nI am a bot 🤖, did i just break?, reply 2 @vishva_nath " %(user_screen_name)

			response = twitter.upload_media(media=photo)
			# message = "@%s Just trying to make a automated system, do not worry. :D,  " %(user_screen_name)
			# i+=1
			twitter.update_status(status=message,in_reply_to_status_id=idd, media_ids=[response['media_id']])

			# twitter.update_status(status=message, in_reply_to_status_id=idd)
			print "~~~~ sent ~~~~\n\n\n~~~~"
			my_set.add(user_screen_name)
		print my_set
	times+=1
