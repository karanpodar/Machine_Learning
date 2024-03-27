"""
jaccard distance is the fraction of intersection divided by union
"""

from sympy import intersection

sentences = ['The bottle is empty', 'There is nothing in the bottle']

def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/ float(union_cardinality)

sentences = [sent.lower().split(" ") for sent in sentences]
print(sentences)
sim = jaccard_similarity(sentences[0], sentences[1])
print(sim)