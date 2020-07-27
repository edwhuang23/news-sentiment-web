import pickle

def restoreTextModel():
    # Restore tuple
    pickled_model, pickled_Xtrain, pickled_Ytrain, pickled_score = pickle.load(open("text_model.pkl", 'rb'))
    return pickled_model, pickled_Xtrain, pickled_Ytrain, pickled_score

def textAnalyze(text):
    return 1

def imageAnalyze(image):
    return 1
