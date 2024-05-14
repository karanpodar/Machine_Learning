import nltk

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize, sent_tokenize, WhitespaceTokenizer, wordpunct_tokenize, regexp_tokenize

text = "Hi! My name iz Karan. Nie to meet you"	
stop_words = stopwords.words('English')
junk_words = ['', ' ', '.', '!']

stop_words.extend(junk_words)
print(stop_words)

words = sent_tokenize(text)   #sentence tokenizer
tokenized_words = word_tokenize(text)   #word tokenizer
white_words = WhitespaceTokenizer().tokenize(text)  # whitespace tokensier removes lines(\n) and whitespaces
punct_words = wordpunct_tokenize(text)  # seperates based on any punctuations also like 3.88 will be '3', '.', '88' 
regex_words = regexp_tokenize(text, pattern=r'\w+|\$[\d\.]+|\S+')   # based on pattern it splits
# print(tokenized_words)