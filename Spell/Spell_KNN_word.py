from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.neighbors import NearestNeighbors

# Load a pre-trained model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def get_word_embedding(word, tokenizer, model):
    # Tokenize the word and get its embedding
    inputs = tokenizer(word, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
    # The embedding of the [CLS] token
    word_embedding = outputs.last_hidden_state[0][0].numpy()
    return word_embedding

# Example words
words = ["machine", "learning", "python", "data", "science", "programming",'cart', "credit", "card"]
embeddings = [get_word_embedding(word, tokenizer, model) for word in words]

# Fit the NearestNeighbors model
neigh = NearestNeighbors(n_neighbors=3, metric='cosine')
neigh.fit(embeddings)

# Example query
query_word = "credt cart"
query_embedding = get_word_embedding(query_word, tokenizer, model).reshape(1, -1)

# Find the nearest words
distances, indices = neigh.kneighbors(query_embedding)

# Display results
for idx in indices[0]:
    print(words[idx])