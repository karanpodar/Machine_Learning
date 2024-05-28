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

chat = model.start_chat(history=[])

response = chat.send_message("In one sentence, explain how a computer works to a young child.")
print(response.text)

print(chat.history)

for message in chat.history:
    print(f'**{message.role}**: {message.parts[0].text}')