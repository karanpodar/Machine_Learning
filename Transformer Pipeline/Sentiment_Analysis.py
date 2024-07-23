'''
https://huggingface.co/learn/nlp-course/chapter1/3?fw=pt
'''

from transformers import pipeline

classifier = pipeline("sentiment-analysis")
print(classifier("I've been waiting for a HuggingFace course my whole life."))

print(classifier(
    ["I've been waiting for a HuggingFace course my whole life.", "I hate this so much!"]
))