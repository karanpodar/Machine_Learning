import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))


txt = "Sukanya, Rajib and Naba are my good friends. " \
	"Sukanya is getting married next year. " \
	"Marriage is a big step in one’s life." \
	"It is both exciting and frightening. " \
	"But friendship is a sacred bond between people." \
	"It is a special kind of love between us. " \
	"Many of you must have tried searching for a friend "\
	"but never found the right one."

# sent_tokenize is one of instances of 
# PunktSentenceTokenizer from the nltk.tokenize.punkt module

tokenized = sent_tokenize(txt)
for i in tokenized:
	
	# Word tokenizers is used to find the words 
	# and punctuation in a string
	wordsList = nltk.word_tokenize(i)

	# removing stop words from wordList
	wordsList = [w for w in wordsList if not w in stop_words]
	print(wordsList)

	# Using a Tagger. Which is part-of-speech 
	# tagger or POS-tagger. 
	tagged = nltk.pos_tag(wordsList)

	print(tagged)


''' Tags list
CC coordinating conjunction 
CD cardinal digit 
DT determiner 
EX existential there (like: “there is” … think of it like “there exists”) 
FW foreign word 
IN preposition/subordinating conjunction 
JJ adjective – ‘big’ 
JJR adjective, comparative – ‘bigger’ 
JJS adjective, superlative – ‘biggest’ 
LS list marker 1) 
MD modal – could, will 
NN noun, singular ‘- desk’ 
NNS noun plural – ‘desks’ 
NNP proper noun, singular – ‘Harrison’ 
NNPS proper noun, plural – ‘Americans’ 
PDT predeterminer – ‘all the kids’ 
POS possessive ending parent’s 
PRP personal pronoun –  I, he, she 
PRP$ possessive pronoun – my, his, hers 
RB adverb – very, silently, 
RBR adverb, comparative – better 
RBS adverb, superlative – best 
RP particle – give up 
TO – to go ‘to’ the store. 
UH interjection – errrrrrrrm 
VB verb, base form – take 
VBD verb, past tense – took 
VBG verb, gerund/present participle – taking 
VBN verb, past participle – taken 
VBP verb, sing. present, non-3d – take 
VBZ verb, 3rd person sing. present – takes 
WDT wh-determiner – which 
WP wh-pronoun – who, what 
WP$ possessive wh-pronoun, eg- whose 
WRB wh-adverb, eg- where, when
'''