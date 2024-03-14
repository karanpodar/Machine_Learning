import spacy
#import contextualSpellCheck
import pandas as pd

nlp = spacy.load("en_core_web_sm")

text = 'Hello! my name is Karan and I am from working as a IT Engineer, i love playing video games'

doc = nlp(text)

for token in doc:
    print(token)

