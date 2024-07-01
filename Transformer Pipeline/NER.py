from transformers import pipeline

ner = pipeline("ner", grouped_entities=True)
print(ner("My name is Sylvain and I work at Hugging Face in Brooklyn."))