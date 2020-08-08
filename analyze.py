import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import nltk
from nltk.stem import WordNetLemmatizer
import re
import ssl
import numpy

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()

from nltk.tokenize import sent_tokenize

def restoreTextModel():
    # Load from file
    with open("text_model.pkl", 'rb') as file:
        pickled_model = pickle.load(file)
        return pickled_model

def textAnalyze(text):
    pickled_model, pickled_Xtrain, pickled_Ytrain, pickled_score = restoreTextModel()

    # Preprocess the text
    # Dictionary of all emojis mapping to their meanings.
    emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad',
              ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
              ':-@': 'shocked', ':@': 'shocked',':-$': 'confused', ':\\': 'annoyed',
              ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
              '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
              '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink',
              ';-)': 'wink', 'O:-)': 'angel','O*-)': 'angel','(:-D': 'gossip', '=^.^=': 'cat'}

    ## Set of all stopwords in english.
    stopwordlist = ['a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an',
                 'and','any','are', 'as', 'at', 'be', 'because', 'been', 'before',
                 'being', 'below', 'between','both', 'by', 'can', 'd', 'did', 'do',
                 'does', 'doing', 'down', 'during', 'each','few', 'for', 'from',
                 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
                 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in',
                 'into','is', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma',
                 'me', 'more', 'most','my', 'myself', 'now', 'o', 'of', 'on', 'once',
                 'only', 'or', 'other', 'our', 'ours','ourselves', 'out', 'own', 're',
                 's', 'same', 'she', "shes", 'should', "shouldve",'so', 'some', 'such',
                 't', 'than', 'that', "thatll", 'the', 'their', 'theirs', 'them',
                 'themselves', 'then', 'there', 'these', 'they', 'this', 'those',
                 'through', 'to', 'too','under', 'until', 'up', 've', 'very', 'was',
                 'we', 'were', 'what', 'when', 'where','which','while', 'who', 'whom',
                 'why', 'will', 'with', 'won', 'y', 'you', "youd","youll", "youre",
                 "youve", 'your', 'yours', 'yourself', 'yourselves']

    # Preprocess data
    processedText = []

    # Create Lemmatizer and Stemmer
    wordLemm = WordNetLemmatizer()

    # Defining regex patterns.
    urlPattern        = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
    userPattern       = '@[^\s]+'
    alphaPattern      = "[^a-zA-Z0-9]"
    sequencePattern   = r"(.)\1\1+"
    seqReplacePattern = r"\1\1"

    tweet = text

    # Make all tweets lowercase
    tweet = tweet.lower()

    # Replace all URLs with 'URL'
    tweet = re.sub(urlPattern,' URL',tweet)

    # Replace all emojis
    for emoji in emojis.keys():
        tweet = tweet.replace(emoji, "EMOJI" + emojis[emoji])

    # Replace @USERNAME to 'USER'
    tweet = re.sub(userPattern,' USER', tweet)

    # Replace all non alphabets
    tweet = re.sub(alphaPattern, " ", tweet)

    # Replace 3 or more consecutive letters by 2 letter
    tweet = re.sub(sequencePattern, seqReplacePattern, tweet)

    tweetwords = ''
    for word in text.split():
        # Checking if the word is a stopword
        # if word not in stopwordlist:
        if len(word) > 1:
          # Lemmatize word
          word = wordLemm.lemmatize(word)
          tweetwords += (word + ' ')

    processedText.append(tweetwords)

    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

    # Vectorize text
    data = vectorizer.transform(processedText)

    response = pickled_model.predict(data)

    if response[0].item() == 4:
        return "positive."
    else:
        return "negative."
