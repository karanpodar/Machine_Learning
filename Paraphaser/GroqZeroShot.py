from groq import Groq
import os

# llama_model = "llama3-70b-8192"

def groq_prompt(user_prompt: str, llama_model="llama-3.1-8b-instant"):
    
    groq_api_key = os.getenv("GROQ_API_KEY")
   
    # groq_api_key = st.secrets["GROQ_API_KEY"]

    client = Groq(api_key=groq_api_key)

    prompt_instruct = f'''
    Paraphrase Generation is the process of presenting and conveying information of original sentence/
phrase in alternative words and order. Paraphrasing text can facilitate reading comprehension by
transforming the text into a more familiar, and in the field of composition, allow writers to restate ideas
from other works or their own drafts so that the reformatted language may better suit a voice, flow, or line
of argument.

You are Alfred, an Intelligent Paraphrasing Assistant for generating custom paraphased passages.
Your objective is to generate a concise and accurate paraphrased answer based solely on the information given by the user.

Instructions:

<instrcutions>
You are an Intelligent Paraphrasing Assistant designed to help users by providing accurate and contextually
relevant answers.
You should generate responses with a minimum length of 80% of the input text length.
Do not answer to inappropriate questions or if there is any profane language used or the user sounds rude. 
</instrcutions>
'''

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_prompt,
            },
            {
                "role": "system",
                "content": prompt_instruct,
            }
        ],
        # model="llama-3.1-8b-instant",
        model=llama_model,
        temperature=0.1,
        max_tokens=450,
    )

    print(chat_completion.choices[0].message.content)

    return chat_completion.choices[0].message.content
