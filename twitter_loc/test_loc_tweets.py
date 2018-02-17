import tweepy
import csv

consumer_key = '7Yh2ff3sSj1K451EzYD6fPmFJ'
consumer_secret = 'eH4aMjOZjf87QFJnRAFSAp3ZBOutoaQpKySqut3zna3alOY9yS'
access_token = '718226343897526272-dggANSmUFnfJcVAxYGND5JvwkGEN74F'
access_token_secret = 'LKQUEtgGKThG7ddh4i8u2F45cdX26ojjiKWdbiktJEmz4'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('tweetsHP.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="*",count=100,geocode="34.0904489,-118.2305523,15km").items(100):
    print [tweet.created_at, tweet.text.encode('utf-8'), tweet.user.id, tweet.geo]
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.user.id])

"""for tweet in tweepy.Cursor(api.search,q="*",count=100,geocode="5.29126,52.132633,150km").items(100):
    print [tweet.created_at, tweet.text.encode('utf-8'), tweet.user.id, tweet.geo]
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),
    tweet.user.id])"""

