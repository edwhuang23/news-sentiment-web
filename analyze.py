import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()

from nltk.tokenize import sent_tokenize

def restoreTextModel():
    # Restore tuple
    pickled_model, pickled_Xtrain, pickled_Ytrain, pickled_score = pickle.load(open("text_model.pkl", 'rb'))
    # # Load from file
    # with open("text_model.pkl", 'rb') as file:
    #     pickle_model = pickle.load(file)
    return pickled_model, pickled_Xtrain, pickled_Ytrain, pickled_score

def textAnalyze(text):
    pickled_model, pickled_Xtrain, pickled_Ytrain, pickled_score = restoreTextModel()

    #vectorizer = TfidfVectorizer()

    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    #vectorizer.transform(pickled_Xtrain)

    # Vectorize text
    data = vectorizer.transform([text])
    # data = sent_tokenize(text)
    # vectorizer.fit_transform(data)

    #query = vectorizer.transform(text)
    return pickled_model.predict(data)

def imageAnalyze(image):
    return 1
