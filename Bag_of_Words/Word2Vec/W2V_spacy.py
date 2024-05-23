import spacy

nlp = spacy.load('en_core_web_md')

sentences = '''The bottle is empty.'''

word = 'glass'

sentences1 = '''There is nothing in the bottle.'''

vec = nlp(sentences).vector
vec1 = nlp(sentences1).vector
# print(vec)

for token in vec:
    print(token.text)

for token in sentences:
    print(token.similarity(word))