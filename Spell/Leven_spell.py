from collections import Counter
import Levenshtein
import string
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from symspellpy import SymSpell
from gensim.models import Word2Vec

# nltk.download('averaged_perceptron_tagger')
# Can Train POS tagging models

stop_words = set(stopwords.words('english'))

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
        if ((self.check_if_word(word) == True)): 
            #and (self.check_if_present(word, comp) == True)):
            
            candidate = []
            d1 = {}
            i = 2
            for x in comp:
                dist = self.leven(word, x)
#                print('in if', word, x, dist)
                if dist <= i:
                    d1[x] = dist
                    candidate.append(x)

            return d1
        
        return word
    
    def check_pos(self, sent):
        pos_word = []
        for i in sent:
            wordsList = nltk.word_tokenize(i)
            wordsList = [w for w in wordsList] 
            tagged = nltk.pos_tag(wordsList)
            print(tagged)
            pos_word.append(tagged)
        return pos_word    
    

#text = 'Hi! 1 My nam is Karan. Whatiz yournam. im Jake'

text = 'Credt cart'


symsp = SymSpell(max_dictionary_edit_distance=0)

symsp.load_dictionary(r'C:\Users\KARAN\Desktop\Python\VsCode_py\python_learn\Spell\Dict.txt',\
                      term_index=0, \
                      count_index=1, \
                      separator=' ')


# Word Segmentation
# test = symsp.word_segmentation(text)
# print(test)

# Loading dictionary keys
comp = symsp.words.keys()

# Word tokenising the input string
#tokenized_words = word_tokenize(test.corrected_string) 
tokenized_words = word_tokenize(text) 

# Preparing dictionary of candidates
Cand = Levencandidates()                  
pred = {}

for x in tokenized_words:
    Test = Cand.candidate(x, comp)
    #print(Test)
    pred[x] = Test.keys()           
    print(f'For input {x} the best candidates are: {Test}')

print(pred)
