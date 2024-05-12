from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# usually converts plural to singular

with open(r"Spell\utter.txt", "r") as file:
    fi = file.read()

lemma = lemmatizer.lemmatize(fi)
print(lemma)

# lemmatizing using POS

lemma1 = lemmatizer.lemmatize('better', pos='a')  # loest form of adjective
print(lemma1)