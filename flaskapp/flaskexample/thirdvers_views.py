from flask import render_template
from flaskexample import app
from flask import request
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
from a_Model import ModelIt


user = 'andric' #add your username here (same as previous postgreSQL)                      
host = 'localhost'
dbname = 'tweetdat'
db = create_engine('postgres://%s%s/%s'%(user,host,dbname))
con = None
con = psycopg2.connect(database = dbname, user = user)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
       title = 'Home', user = { 'nickname': 'Miguel' },
       )

@app.route('/db')
def firsttweets():
    sql_query = """                                                                       
                SELECT * FROM la_tweets LIMIT 7;          
                """
    query_results = pd.read_sql_query(sql_query, con)
    tweets = ""
    print query_results[:7]
    for i in range(7):
        tweets += query_results.iloc[i]['tweet']
        tweets += "<br>"
    return tweets 

@app.route('/db_fancy')
def tweets_res_fancy():
    sql_query = """
                SELECT username, user_tweet_count, rt_count FROM la_tweets LIMIT 7;
                """
    query_results = pd.read_sql_query(sql_query, con)
    print query_results
    tweets = []
    for i in range(0, query_results.shape[0]):
	tweets.append(dict(username=query_results.iloc[i]['username'], user_tweet_count=query_results.iloc[i]['user_tweet_count'], rt_count=query_results.iloc[i]['rt_count']))
        return render_template('tweetinfo.html', tweets=tweets)

@app.route('/input')
def tweets_input():
    return render_template("input.html")

@app.route('/output')
def tweets_output():
  #pull 'rt_count' from input field and store it
  rt_number = request.args.get('rt_count')
  query = "SELECT username, user_tweet_count, rt_count FROM la_tweets WHERE rt_count > '%s'" % rt_number
  print query
  query_results=pd.read_sql_query(query,con)
  print query_results
  tweets = []
  for i in range(0,query_results.shape[0]):
      tweets.append(dict(username=query_results.iloc[i]['username'], user_tweet_count=query_results.iloc[i]['user_tweet_count'], rt_count=query_results.iloc[i]['rt_count']))
      the_result = ''
      the_result = ModelIt(rt_number, tweets)
  return render_template("output.html", tweets = tweets, the_result = the_result)