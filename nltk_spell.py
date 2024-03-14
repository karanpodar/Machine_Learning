import nltk

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hi! My name iz Karan. Nie to meet you"	
stop_words = stopwords.words('English')
junk_words = ['', ' ', '.', '!']

stop_words.extend(junk_words)
print(stop_words)

#words = sent_tokenize(text)   #sentence tokenizer
tokenized_words = word_tokenize(text)   #word tokenizer
print(tokenized_words)

# syn = wordnet.synsets('Computer')
# print(syn[0].definition())