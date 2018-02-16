import csv
import tweepy
from nltk.corpus import stopwords
from nltk import word_tokenize
import nltk
import matplotlib
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer
import re
import pandas as pd

consumer_key = '7Yh2ff3sSj1K451EzYD6fPmFJ'
consumer_secret = 'eH4aMjOZjf87QFJnRAFSAp3ZBOutoaQpKySqut3zna3alOY9yS'
access_key = '718226343897526272-dggANSmUFnfJcVAxYGND5JvwkGEN74F'
access_secret = 'LKQUEtgGKThG7ddh4i8u2F45cdX26ojjiKWdbiktJEmz4'
 
def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print("...%s tweets downloaded so far" % (len(alltweets)))
    
    #transform the tweepy tweets into a 2D array that will populate the csv    
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    
    #write the csv    
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)
    
    pass


#download the tweets
get_all_tweets('@realDonaldTrump')


#load into a pandas data frame
df = pd.DataFrame.from_csv('@realDonaldTrump_tweets.csv')


#get the top words
top_N = 10

txt = df.text.str.lower().str.replace(r'\|', ' ').str.cat(sep=' ')
# txt = 

txt = txt.replace('https','')
txt = txt.replace('.co','')

tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(txt)

# words = nltk.tokenize.word_tokenize(txt)
word_dist = nltk.FreqDist(words)

stopwords = nltk.corpus.stopwords.words('english')
words_except_stop_dist = nltk.FreqDist(w for w in words if w not in stopwords) 

print('All frequencies, including STOPWORDS:')
print('=' * 60)
rslt = pd.DataFrame(word_dist.most_common(top_N),
                    columns=['Word', 'Frequency'])
print(rslt)
print('=' * 60)

rslt = pd.DataFrame(words_except_stop_dist.most_common(top_N),
                    columns=['Word', 'Frequency']).set_index('Word')



matplotlib.style.use('ggplot')

rslt.plot.bar(rot=0)
plt.title('Trump Top Words')
