from nltk.corpus import wordnet

syns = wordnet.synsets("program")

print(syns[0])
print(syns[0].lemmas()[0].name())

