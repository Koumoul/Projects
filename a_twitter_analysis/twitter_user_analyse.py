import tweepy
import sqlite3
import sys
import os.path
import operator
#---------------------------- IDENTIFICATION -----------------------------------
consumer_key = 'uwxi4v0OJcyMNfu6knSAXF3mU'
consumer_secret = 'OWj7lrj4pSv4LgNGL95yevtMEHbn55YIg2iaaBTsf8LV6kiUZd'
access_token = '730395298959364096-G9tbilOjNyq9kk8ANmXCN2jC4aSF3ro'
access_token_secret = 'L3iQdrhuxZrUeDtqNDdQcj8SuhMszzf5Wl2nFgLQChjh0'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
API = tweepy.API(auth)
#-------------------------------------------------------------------------------

print("Welcome")
print("")
name = input('User screen name:')

user = API.get_user(name)
followers = API.followers_ids(name, [-1])
timeline = API.user_timeline(name)
print("You are working on: ",user.screen_name,"\nHe have ",user.followers_count," followers.")
#---------------------------- CREATION DOSSIER ---------------------------------
path = '/Users/Nicolas/Desktop/Twitter_py/' + name
if not os.path.exists(path):
    os.mkdir(path)
#---------------------------- COLLECTE DES DONNEES / SQLite3 -----------------------------

conn = sqlite3.connect(path+'/'+ name +'_followers.db')
c = conn.cursor()
c.execute('''CREATE TABLE followers
             (screen_name TEXT, name TEXT, id INTEGER, lang TEXT)''')

f = API.get_user('roskonewz')
c.execute("INSERT INTO followers(screen_name,name,id,lang) VALUES(f.screen_name,f.name,f.id,f.lang)")
conn.commit()
c.close()
conn.close()
