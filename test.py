import tweepy
import json
import pandas as pd
import time
import os
import sys
import wget
import requests

def getTweetsFromUser(username,no_of_tweets,api):
	## Fetches Tweets from user with the handle 'username' upto max of 'no_of_tweets' tweets
	last_tweet_id = 0

	raw_tweets = api.user_timeline(screen_name=username,include_rts=False,exclude_replies=True)

	print(raw_tweets)

	last_tweet_id = int(raw_tweets[-1].id-1)
	
	print ('\nFetching tweets.....')

	while len(raw_tweets)<no_of_tweets:
		sys.stdout.write("\rTweets fetched: %d" % len(raw_tweets))
		sys.stdout.flush()
		temp_raw_tweets = api.user_timeline(screen_name=username, max_id=last_tweet_id, include_rts=False, exclude_replies=True)
		if len(temp_raw_tweets) == 0:
			break
		else:
			last_tweet_id = int(temp_raw_tweets[-1].id-1)
			raw_tweets = raw_tweets + temp_raw_tweets

	print ('\nFinished fetching ') + str(min(len(raw_tweets),no_of_tweets)) + ' Tweets.'
	return raw_tweets

def getTweetMediaURL(all_tweets):
	print ('\nCollecting Media URLs.....')
	tweets_with_media = set()
	for tweet in all_tweets:
		media = tweet.entities.get('media',[])
		if (len(media)>0):
			tweets_with_media.add(media[0]['media_url'])
			sys.stdout.write("\rMedia Links fetched: %d" % len(tweets_with_media))
			sys.stdout.flush()
	print ('\nFinished fetching ') + str(len(tweets_with_media)) + ' Links.'

	return tweets_with_media

def downloadFiles(media_url,username):
	print ('\nDownloading Images.....')
	try:
	    os.mkdir('twitter_images')
	    os.chdir('twitter_images')
	except:
		os.chdir('twitter_images')

	try:
	    os.mkdir(username)
	    os.chdir(username)
	except:
		os.chdir(username)

	for url in media_url:
		wget.download(url)


def main():
    f = open('config.json')
    data = json.load(f)

    #Pass in our twitter API authentication key
    auth = tweepy.OAuth1UserHandler(
        data['consumer_key'], data['consumer_secret'],
        data['access_token'], data['access_token_secret']
    )

    #Instantiate the tweepy API
    api = tweepy.API(auth, wait_on_rate_limit=True)

    username = "coinfessions"
    no_of_tweets =10
    all_tweets = getTweetsFromUser(username,no_of_tweets,api)

    try:
        #all_tweets = getTweetsFromUser(username,no_of_tweets,api)
        media_URLs = getTweetMediaURL(all_tweets)
        #downloadFiles(media_URLs,username)
        print ('\n\nFinished Downloading.\n')

    except BaseException as e:
        print('Status Failed On,',str(e))
        time.sleep(3)

if __name__ == "__main__":
    main()


for name in filenames:
    # Save text from image to "new_text" variable
    path = Path('lib\\images\\coinfessions\\' + name)
    text = create_text(path)
    words = text.split()
    new_text = " ".join(words[1:])