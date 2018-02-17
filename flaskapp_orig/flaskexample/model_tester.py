from sklearn.externals import joblib
import numpy as np
from textblob import TextBlob


def extract_hash_tags(s):
    return set(part[1:] for part in s.split() if part.startswith('#'))

def extract_http(s):
    return set(part for part in s.split() if part.startswith('http'))

def get_features(tweet_str):
    twt = TextBlob(tweet_str.decode('utf-8'))
    verblist = list()
    pronlist = list()
    for word, tag in twt.tags:
        if 'VB' in tag:
            verblist.append(word.lemmatize())
        if tag == 'PRP':
            pronlist.append(word.lemmatize())
    try:
        repeat_word_penalty = len(twt.word_counts.values()) / sum(twt.word_counts.values())
    except ZeroDivisionError:
        repeat_word_penalty = 1
    return (twt.sentiment.polarity, twt.sentiment.subjectivity, len(twt.noun_phrases), repeat_word_penalty,
            len(twt.words), len(extract_hash_tags(twt)), len(extract_http(twt)),
            len(verblist), len(pronlist))


def rand_forest(input_text):
    model_dir = '/Users/andric/Documents/workspace/insight/twitter_loc/model_dir/'
    rf_model = joblib.load('%s/forest_model.sav' % model_dir)
    outclass = rf_model.predict(np.array(get_features(input_text)).reshape(1, -1))[0]
    outprob = np.max(rf_model.predict_proba(np.array(get_features(input_text)).reshape(1, -1))[0])
    return (outclass, outprob)

