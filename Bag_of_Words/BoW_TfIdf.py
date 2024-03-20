from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize, word_tokenize

# create the transform
vectorizer = TfidfVectorizer()

with open(r"Spell\utter.txt", "r") as file:
    fi = file.read()

text = sent_tokenize(fi)

# tokenize and build vocab
vectorizer.fit(text)

# summarize
print(sorted(vectorizer.vocabulary_))

# encode document
vector = vectorizer.transform(text)
print(vectorizer.idf_)
print(vector)

# summarize encoded vector
print(vector.shape)
print(vector.toarray())