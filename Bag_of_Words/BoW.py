import nltk 
import re
import numpy as np 
from nltk.tokenize import sent_tokenize, word_tokenize


with open(r"Spell\utter.txt", "r") as file:
    fi = file.read()

dataset = sent_tokenize(fi)
print(dataset)
print(len(dataset))
for i in range(2): 
    dataset[i] = dataset[i].lower() 
    dataset[i] = re.sub(r'\W', ' ', dataset[i])    # to match alphanumeric values
    dataset[i] = re.sub(r'\s+', ' ', dataset[i])   # to match more than 1 whitespace


word2count = {} 
for data in dataset: 
    words = word_tokenize(data) 
    for word in words: 
        if word not in word2count.keys(): 
            word2count[word] = 1
        else: 
            word2count[word] += 1

# print(word2count)


X = [] 
for data in dataset: 
    vector = [] 
    for word in word2count:
#        print(word, data) 
        if word in nltk.word_tokenize(data): 
            vector.append(1) 
        else: 
            vector.append(0) 
    X.append(vector) 
 
X = np.asarray(X)

# print(X)
# print(vector)