from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('stsb-roberta-large')

sentences = []
embeddings = model.encode(sentences, convert_to_tensor=True)