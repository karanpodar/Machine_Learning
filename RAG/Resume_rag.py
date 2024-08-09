import nltk
from nltk.tokenize import sent_tokenize
import faiss
import openai
from sentence_transformers import SentenceTransformer
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

import requests
import os

# Download necessary NLTK data
# nltk.download('punkt')

openai_api_key = os.getenv('OPENAI_API_KEY')
hf_api_key = os.getenv('HF_TOKEN')
# claude_api_key = os.getenv('CLAUDE_API_KEY')

class ResumeRAG:
    # claude_api_key = os.getenv('CLAUDE_API_KEY')
    def __init__(self, resume_text, openai_api_key, hf_api_key):
        self.resume_text = resume_text
        self.sentences = sent_tokenize(resume_text)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.sentence_embeddings = self.model.encode(self.sentences)
        
        # Initialize FAISS index
        self.dimension = self.sentence_embeddings.shape[1]
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(self.sentence_embeddings.astype('float32'))

        # Set up OpenAI API
        openai.api_key = openai_api_key

        # Hugging Face API setup
        self.hf_api_url = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
        self.headers = {"Authorization": f"Bearer {hf_api_key}"}

    def get_most_relevant_sections(self, query, k=3):
        # Encode the query
        query_embedding = self.model.encode([query])[0]
        
        # Search the FAISS index
        distances, indices = self.index.search(query_embedding.reshape(1, -1).astype('float32'), k)
        
        relevant_sections = [self.sentences[i] for i in indices[0]]
        return relevant_sections

    def call_claude_api(self, prompt):
        # Placeholder for Claude API call
        # Replace this with actual API call to Claude
        claude_api_key = os.getenv('CLAUDE_API_KEY')
        # api_url = "https://api.anthropic.com/v1/chat/completions"
        api_url = "https://api.anthropic.com/v1/messages"
        headers = {
            "Authorization": f"Bearer {claude_api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "claude-3-sonnet-20240229",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1000
        }
        response = requests.post(api_url, headers=headers, json=data)
        print(response)
        return response.json()['choices'][0]['message']['content']
    
    def call_openai_api(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on the given resume information."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    
    def call_llama_api(self, prompt):
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 150,
                "temperature": 0.7,
                "top_p": 0.95,
                "do_sample": True,
            }
        }
        response = requests.post(self.hf_api_url, headers=self.headers, json=payload)
        print(response)
        return response.json()[0]['generated_text']
    
    def answer_question(self, question):
        relevant_sections = self.get_most_relevant_sections(question)
        context = " ".join(relevant_sections)
        
        prompt = f"""Based on the following resume information:

{context}

Please answer the following question:
{question}

Provide a concise and accurate answer based solely on the information given in the resume context.
If the information is not available in the context, please state that it cannot be determined from the given information."""

        print(prompt)
        answer = self.call_claude_api(prompt)
        # answer = self.call_openai_api(prompt)
        # answer = self.call_llama_api(prompt)
        print('answer is this', answer)
        return answer


with open(r'RAG\resume.txt', 'r', encoding="utf8") as f1:
    resume_text = f1.read()


print(resume_text)
    
rag = ResumeRAG(resume_text, openai_api_key, hf_api_key)

# Example questions
# questions = [
#     "What is Karan's email address?",
#     "How many years of experience does John have?",
#     "What programming languages does John know?",
#     "Where did John go to college?",
#     "What was John's role at Tech Corp?"
# ]

questions = ["What is Karan's email address?"]

for question in questions:
    print(f"Q: {question}")
    print(f"A: {rag.answer_question(question)}\n")