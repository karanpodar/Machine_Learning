import torch
from transformers import BertTokenizer, BertModel

# Initialize the tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Input sentence
sentence = "Transformers provide state-of-the-art results for many NLP tasks."

# Tokenize the input sentence
inputs = tokenizer(sentence, return_tensors='pt')

# Get the outputs from the model
with torch.no_grad():
    outputs = model(**inputs)

# Extract the last hidden states (embeddings)
last_hidden_states = outputs.last_hidden_state

# Convert token IDs to tokens
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])

# Print the tokens and their corresponding embeddings
for token, embedding in zip(tokens, last_hidden_states[0]):
    print(f"Token: {token}, Embedding: {embedding[:5]}")  # Printing only the first 5 dimensions for brevity