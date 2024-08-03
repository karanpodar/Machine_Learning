import anthropic
from nltk.tokenize import sent_tokenize
import faiss
from sentence_transformers import SentenceTransformer
from langchain.prompts import ChatPromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

import requests
import os


client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.getenv('CLAUDE_API_KEY'),
)

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    messages=['what is the clolor of sky']
)
print(message.content)