import string

print(string.punctuation)

word = 'Hello! My name is Karan. What is your name?'

test_str = word.translate(str.maketrans('', '', string.punctuation))
print(test_str)