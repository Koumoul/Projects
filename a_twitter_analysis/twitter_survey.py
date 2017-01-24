import tweepy
import sqlite3
import sys
import os.path
import twitter

#---------------------------- IDENTIFICATION -----------------------------------
consumer_key = 'uwxi4v0OJcyMNfu6knSAXF3mU'
consumer_secret = 'OWj7lrj4pSv4LgNGL95yevtMEHbn55YIg2iaaBTsf8LV6kiUZd'
access_token = '730395298959364096-G9tbilOjNyq9kk8ANmXCN2jC4aSF3ro'
access_token_secret = 'L3iQdrhuxZrUeDtqNDdQcj8SuhMszzf5Wl2nFgLQChjh0'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
API = tweepy.API(auth)

user = 'roskonewz'
friends = API.friends_ids(user, [-1])
#fichier = open('/Users/Nicolas/Desktop/Twitter_py/survey/tweet.txt', "x")

for following in friends:
    f = API.get_user(following)
    for statuses in tweepy.Cursor(API.user_timeline, screen_name=f.screen_name, include_rts=False).items(20):

        fichier = open('/Users/Nicolas/Desktop/Twitter_py/survey/tweet.txt', "a")
        fichier.write(f.screen_name + "   : " + statuses.text + " \n ** \n ")
        fichier.close
#-------------------------------------------------------------------------------
