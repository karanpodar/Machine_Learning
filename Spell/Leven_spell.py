from collections import Counter
import Levenshtein
import string
from nltk.tokenize import word_tokenize
from symspellpy import SymSpell


class Levencandidates:

    def __init__(self, word=None, comp=None):
        self.word = word
        self.comp = comp

    def leven(self, x, y):
        return Levenshtein.distance(x,y)

    def check_if_present(self, word, comp):
        for y in comp:
            if word in comp:
                return False
            else:
                pass
        return True

    def check_if_word(self, word):
        if len(word) == 1 and word in string.punctuation:
            return False
        try:  # check if it is a number (int, float, etc)
            float(word)
            return False
        except ValueError:
            pass
        return True

    def candidate(self, word, comp):
        if ((self.check_if_word(word) == True) and (self.check_if_present(word, comp) == True)):
            candidate = []
            d1 = {}
            for x in comp:
                dist = self.leven(word, x)
#                print('in if', word, x, dist)
                if dist <= 2:
                    d1[x] = dist
                    candidate.append(x)
            return d1
        return word

text = 'Hi! 1 My nam is Karan. Whatiz yournam. im Jake'

symsp = SymSpell(max_dictionary_edit_distance=0)

symsp.load_dictionary('Dict.txt',\
                      term_index=0, \
                      count_index=1, \
                      separator=' ')

test = symsp.word_segmentation(text)
print(test)

comp = symsp.words.keys()
#print(comp)

tokenized_words = word_tokenize(test.corrected_string) 

# with open("Test_Dict.txt", "r") as infile:
#     comp = word_tokenize(infile.read())

Cand = Levencandidates()                  

for x in tokenized_words:
    # input.append(x) 
    Test = Cand.candidate(x, comp)                    
    print(f'For input {x} the best candidates are: {Test}')

