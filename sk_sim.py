import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Convert the texts into TF-IDF vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(['Table', 'T@ble'])

# Calculate the cosine similarity between the vectors
similarity = cosine_similarity(vectors)
print(similarity)