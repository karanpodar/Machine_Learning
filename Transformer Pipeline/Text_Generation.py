from transformers import pipeline

generator = pipeline("text-generation")
print(generator("In this course, we will teach you how to"))