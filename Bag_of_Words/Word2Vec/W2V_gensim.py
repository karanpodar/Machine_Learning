from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize, word_tokenize

sentences = ('''The bottle is empty.
There is nothing in the bottle.
Please refill the bottle.''')

temp = []

# tokenize the sentences into words
for j in word_tokenize(sentences, 'english'):
    temp.append(j.lower())
 
print(temp) 

# Create Word2Vec - CBOW
model = Word2Vec([temp], vector_size=100, window=5, min_count=1, workers=4)

sim_words = model.wv.most_similar('bottle')
print(model.wv.index_to_key)
print(sim_words)

# Print results
# print("Cosine similarity between 'bottle' " +
#       "and 'refill' - CBOW : ",
#       model.wv.distance('bottle', 'refill'))

# Create Skip Gram model
# model2 = Word2Vec([temp], min_count=1, vector_size=100,
#                                 window=5, sg=1)

# print(model2.wv.index_to_key)

# # Print results
# print("Cosine similarity between 'bottle' " +
#       "and 'refill' - Skip-Gram : ",
#       model2.wv.distance('bottle', 'refill'))
