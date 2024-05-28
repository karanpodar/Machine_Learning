# pip install google-generativeai
# to set GOOGLE_API_KEY as env variable you need to update the details in system variables

import os

import google.generativeai as genai

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
print(GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)


for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)


model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")

#to check the feedback in case the response was not generated 
print(response.prompt_feedback)

# to check the other candidate answers
print(response.candidates)
