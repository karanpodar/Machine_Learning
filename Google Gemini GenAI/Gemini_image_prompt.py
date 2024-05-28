# pip install google-generativeai
# to set GOOGLE_API_KEY as env variable you need to update the details in system variables

import os
import textwrap
import PIL.Image

import google.generativeai as genai

img = PIL.Image.open('image.jpg')
print(img)


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
print(GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)


model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(img)

# to get the details of the image
print(response.text)

# to generate a response related to prompt based on image
response = model.generate_content(["Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.", img], stream=True)
response.resolve()
print(response.text)

#to check the feedback in case the response was not generated 
print(response.prompt_feedback)

# to check the other candidate answers
print(response.candidates)
