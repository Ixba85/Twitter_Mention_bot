import tweepy
import time
# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.
from credentials import *

# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/
print('this is my bot', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline( since_id = last_seen_id, tweet_mode='extended')
    
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        since_id = mention.id
        store_last_seen_id(since_id, FILE_NAME)
        if '#randomrecipe' in mention.full_text.lower():
            print('found #randomrecipe')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + '  https://www.randomlists.com/random-recipes, Here it is!', in_reply_to_status_id = mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)