# News Sentiment Analysis

This is a tool that analyzes the sentiment of text and images that frequently appear in the news. Check out https://news-sentiment-web.herokuapp.com/home to start analyzing sentiments!

## Text Analysis
To analyze the text, we trained scikit-learn's linear support vector machine (LinearSVC) using 1.6 million tweets that were preprocessed (some things we did include stemming and lemmatizing the content). We first used a HashingVectorizer to vectorizer the tweets.
In other words, we converted all the content into word embeddings (also known as word vectors) which is essentially a mathematical vector representation for a word before we fit the SVC model.

## Image Analysis
