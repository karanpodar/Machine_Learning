from textblob import TextBlob

a = "Hi! My name iz Karan. Nie to meet you"		 # incorrect spelling
print("original text: "+str(a))

b = TextBlob(a)

# prints the corrected spelling
print("corrected text: "+str(b.correct()))
