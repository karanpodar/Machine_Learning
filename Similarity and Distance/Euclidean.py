"""
Shortest distance between 2 points, can be calucated as the hypotenuse of a pythagoras theorem
"""

from math import sqrt, pow, exp
import spacy

nlp = spacy.load('en_core_web_md')

def squared_sum(a):
    return round(sqrt(sum([x*x for x in a])), 3)

def euclidean(x,y):
    return sqrt(sum(pow(a-b, 2) for a, b in zip(x, y)))

def distance_to_similarity(x):
    return 1/exp(x)

sentences = '''The bottle is empty.'''

sentences1 = '''There is nothing in the bottle.'''

vec = nlp(sentences).vector
vec1 = nlp(sentences1).vector

dist = euclidean(vec, vec1)

dist_sim = distance_to_similarity(dist)

print(dist)
print(dist_sim)
