from sklearn.feature_extraction.text import HashingVectorizer
from nltk.tokenize import sent_tokenize, word_tokenize


# create the transform
vectorizer = HashingVectorizer(n_features=6)

with open(r"Spell\utter.txt", "r") as file:
    fi = file.read()

text = sent_tokenize(fi)


# encode document
vector = vectorizer.transform(text)
print(vector)

# summarize encoded vector
print(vector.shape)
print(vector.toarray())