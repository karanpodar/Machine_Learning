import pandas as pd
import time
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import semantic_search

inp = input('What do you want to search?\n')

start = time.process_time()

df = pd.read_csv('Barclays_FAQs.csv', encoding='cp1252')

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
embeddings = model.encode(inp)
r = semantic_search(embeddings, model, top_k=30)[0]
idx = [x['corpus_id'] for x in r]

result = ( df[idx].head(20) )


end = time.process_time()

print(result)
print('time', end - start)