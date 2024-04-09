import pandas as pd
import numpy as np
import re
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.stem.porter import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as VS
from textstat.textstat import *
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import joblib

# Define the preprocess function
def preprocess(text):
  spacepattern='\s+'
  urlregex=('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|''[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
  mentionregex='@[\w\-]+'
  parsedtext=re.sub(spacepattern, " ", text)
  parsedtext=re.sub(urlregex,"",parsedtext)
  parsedtext=re.sub(mentionregex,"",parsedtext)
  return parsedtext

# Define the tokenize function
def tokenize(tweet):
  tweets=" ".join(re.split("[^a-zA-Z]*", tweet.lower())).strip()
  tokens=[]
  for t in tweets.split():
    tokens.append(stemmer.stem(t))
  return tokens

# Load the saved model
model = joblib.load('model/hatespeachmodel.pkl')

# Load the vectorizer
vectorizer = joblib.load('model/vectorizer.joblib')

# Assume we have a list of sentences
sentences = ["This is the first sentence.", "This is another sentence."]

stopwords = nltk.corpus.stopwords.words("english")
exclusions = ["#ff", "ff", "rt", "austrian painter"]
stopwords.extend(exclusions)
stemmer = PorterStemmer()

# Transform the sentences into TF-IDF vectors
sentence_tfidf = vectorizer.transform(sentences)

# Use the loaded model to predict the classes of the sentences
predictions = model.predict(sentence_tfidf)

print(predictions)