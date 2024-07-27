from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import numpy as np
import pandas as pd

# create the transform
vectorizer = CountVectorizer()

with open(r"Spell\utter.txt", "r") as file:
    fi = file.read()

text = sent_tokenize(fi)

vectorizer.fit(text)

print(vectorizer.get_feature_names_out())

# print(vectorizer.vocabulary_)
# print(len(vectorizer.vocabulary_))

bag_of_words = vectorizer.transform(text)

# print(bag_of_words)
# print(bag_of_words.shape)

bag_of_words = bag_of_words.toarray()

# print(bag_of_words)
# print(bag_of_words.shape)

# df = pd.DataFrame(bag_of_words)

# print(df.head())

# Divide Data into Training and Test Sets
X_train, X_test = train_test_split(text,  test_size=0.30, random_state=0)

print(X_train)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

rf_clf = RandomForestClassifier(random_state=42, n_estimators=500)

classifier = rf_clf.fit(X_train)
