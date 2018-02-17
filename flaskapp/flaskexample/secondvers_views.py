from flask import render_template
from flaskexample import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2

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
    for i in range(7):
        tweets += query_results.iloc[i]['tweet']
        tweets += "<br>"
    return tweets 
