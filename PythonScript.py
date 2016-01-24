import tweepy 
import csv
import json
from textblob import TextBlob 
import re
import xlrd
import unicodedata
import time


consumer_key = "3Dls6VgL4VdGUfRMoKYRwQ7sK"
consumer_secret = "UmL3mksCxByDCyNORvUylSrjqTD1p4DD9HowQrwzgYXBPs8afl"
access_key = "577199497-dgnR4EvXpMNdmqsf88e2TRpwW3BVCKjtxNYY9zQM"
access_secret = "88loffXsVnShh1VBkAPuO9oKHykRl6dENiYw4v6WNe2fH"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

relationship = ['hate', 'left', 'bf','gf','girlfriend','boyfriend','heartbreak','alone', 'love']
education = ['exam','test','assignment','school']
money = ['broke','money','cash','economy', 'finance','crisis']

# gets latest tweets of user
def get_tweets_for_user(screen_name):
	latest_tweets = api.user_timeline(screen_name = screen_name,count=200)
	outtweets = [[tweet.user.location, tweet.coordinates, tweet.text.encode("utf-8"), screen_name] for tweet in latest_tweets]
	for x in range(len(outtweets) - 1,-1,-1):
		tweets = outtweets[x]
		try:
			#do sentiment analysis
			temp = TextBlob(re.sub(r'[^a-zA-Z0-9 ]',r'',tweets[2]))
			tweets.append(temp.sentiment.polarity)
			if temp.sentiment.polarity < 0:
				if  any(y in tweets[2] for y in relationship):
					tweets.append(1)
				else:
					tweets.append(0)
				
				if  any(y in tweets[2] for y in education):
					tweets.append(1)
				else:
					tweets.append(0)
				if  any(y in tweets[2] for y in money):
					tweets.append(1)
				else:
					tweets.append(0)
			else:
				# not including positive tweets
				outtweets.pop(x)
				
			
		except Exception,e:
			outtweets.pop(x)
		finally:
			pass
	#write the csv
	with open('tweets.csv', 'ab') as f:
		writer = csv.writer(f)
		writer.writerows(outtweets)

def analyze_all_users():
	call_count = 1
	try:
		file_location = "D:\Hackathon\TwitterUserList.xlsx"
		workbook = xlrd.open_workbook(file_location)
		sheet = workbook.sheet_by_index(0)
		
		
		for row in range(sheet.nrows):
			val= sheet.cell_value(row,0)
			#Twitter allows only 180 queries in 15 min (using 150 and 16 mins)
			if call_count%150==0:
				time.sleep(960)
			try:
				call_count = call_count + 1
				get_tweets_for_user(val)
			except Exception,e:
				pass
	finally:
		pass
	
analyze_all_users()