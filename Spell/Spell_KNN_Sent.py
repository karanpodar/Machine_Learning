from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example documents
documents = [
    "This is a document about machine learning.",
    "This is a document all about machine learning.",
    "This is a document everything about machine learning.",
    "These are the documents everything about machine learning.",
    "These are the documents all about machine learning.",
    "Another document discussing Python and data science.",
    "More content related to natural language processing."
]

# Convert documents to embeddings
embeddings = model.encode(documents)

# Fit the NearestNeighbors model
neigh = NearestNeighbors(n_neighbors=3, metric='cosine')
neigh.fit(embeddings)

# Example query
query = "This is a docment about mahine learning."

# Convert query to embedding
query_embedding = model.encode([query])

# Find the nearest documents
distances, indices = neigh.kneighbors(query_embedding)

# Display results
for idx in indices[0]:
    print(documents[idx])

