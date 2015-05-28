# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:39:37 2015

@author: sushantobeja
"""

import tweepy
import csv


consumer_key = 'ilLdUTZDWRoPHwbr1eTQ16lum'
consumer_secret = 'cSkt89WrDJKd59Tf3oJbMKCjuIne8Y1phSvKlq2O6BvJ4ltg9Q'
access_token = '3040203180-QT4Sbn7ssm5WyqXM3p9AtODo4CBxt0ErzKGTTPr'
access_token_secret = 'NpTadXj8aabfUnt9HpbYC3nbWU4JQhw0aRrecaNnjdlvZ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('University_of_minnesota_tweets.csv', 'w')
#Use csv Writer
csvWriter = csv.writer(csvFile)
count=0
for tweet in tweepy.Cursor(api.search,q="",count=100,\
                           geocode = "44.975021,-93.235612,3km",\
                           lang="en",\
                           since_id=2015-01-01).items():
    print tweet.created_at, tweet.text
    count=count+1
    csvWriter.writerow('*******************************************************')
    csvWriter.writerow([tweet.id,tweet.created_at,tweet.text.encode('utf-8')])
    print count    

    
