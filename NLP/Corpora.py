import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

nltk.download('gutenberg')

# C:\Users\KARAN\AppData\Roaming\nltk_data\corporas

sample = gutenberg.raw("shakespeare-macbeth.txt")
tok = sent_tokenize(sample)

print(tok[:15])