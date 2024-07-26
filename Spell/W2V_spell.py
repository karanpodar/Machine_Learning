from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize, word_tokenize

with open(r"Spell\utter.txt", "r") as file:
    fi = file.read()

token_word = word_tokenize(fi)

model = Word2Vec([token_word], vector_size=100, window=5, min_count=1, epochs=10, workers=4)

# print(model.wv.index_to_key)

test_input = 'credt cart'

input_token = word_tokenize(test_input)

for x in input_token:
    pred_sim = model.wv.most_similar(x)
    print(pred_sim)