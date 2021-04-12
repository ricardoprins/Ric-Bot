import random
import pandas as pd
import os
import urllib
import praw
import datetime
import json
from get_secrets import SecretsStore

def get_memes():
   '''Function to get and post memes in a discord server '''
   
   user_agent = "Ric-Bot - Discord bot by Tesseract Coding"
   store = SecretsStore()
   secrets_data = store.get_all_secrets()
   reddit = praw.Reddit(client_id = secrets_data["REDDIT_CLIENT_ID"], 
                        client_secret = secrets_data["REDDIT_CLIENT_SECRET"], 
                        user_agent = user_agent)
   subreddit = reddit.subreddit('funnyterriblefacebookmemes+wholesomememe+ProgrammerHumor+MemeEconomy+memes+dankmemes+AdviceAnimals')
   
   posts = subreddit.hot(limit=21)

   image_urls, image_titles = [], []
   allowed_image_extensions = ['.jpg', '.jpeg', '.png']

   for post in posts:
      image_urls.append(post.url.encode('utf-8'))
      image_titles.append(post.title.encode('utf-8'))
   
   lenUrl = len(image_urls)

   for i in range(lenUrl):
      modstring = str(image_urls[i]).split("b'")[1]
      modstring = modstring[:-1]
      image_urls[i] = modstring
      
   return image_urls[random.randint(0,20)]
