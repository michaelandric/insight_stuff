from flask import render_template
from flaskexample import app
from flask import request
from a_Model import ModelIt
from model_tester import rand_forest
from collections import Counter


@app.route('/')
@app.route('/index')
def tweets_input():
    return render_template("input.html")

@app.route('/output')
def tweets_output():
    tweet_box_text = request.args.get('tweetbox')
    tweet_text = tweet_box_text.decode('utf-8')
    print tweet_text
    if sum(Counter(tweet_text).values()) > 140:
        return "Oh no! You need to use less than 140 characters!"
    else:
        outclasspred, outclasspredprob = rand_forest(tweet_text)
        classprobpercnt = outclasspredprob * 100
        classpercnt = "%.1f%%" % classprobpercnt
        if outclasspred == 0 and outclasspredprob > .74:
            classmessage = "No good! You should really try again!"
        elif outclasspred == 0:
            classmessage = "You could do better."
        if outclasspred == 1 and outclasspredprob > 75:
            classmessage = "Good work! You're on your way to being a social media star!"
        elif outclasspred == 1: 
            classmessage = "This is pretty good. But you can improve."
        return render_template("output.html", classpred = classmessage, classprob = classpercnt)

