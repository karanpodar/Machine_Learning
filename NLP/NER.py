import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import treebank

nltk.download(['maxent_ne_chunker', 'words', 'treebank'])

with open(r"Spell\utter.txt", "r") as file:
    fi = file.read()

tokens = word_tokenize(fi)

# print(tokens)

tagged = nltk.pos_tag(tokens)

# print(tagged)

entities = nltk.chunk.ne_chunk(tagged)

print(entities)

t = treebank.parsed_sents('wsj_0001.mrg')[0]

entities.draw()