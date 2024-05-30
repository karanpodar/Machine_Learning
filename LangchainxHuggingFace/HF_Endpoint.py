import os
from langchain_huggingface import HuggingFaceEndpoint
# from langchain_community.llms import HuggingFaceEndpoint

os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv('HUGGINGFACEHUB')
tok_id = os.environ['HUGGINGFACEHUB_API_TOKEN']

repo="meta-llama/Llama-2-7b-hf"
llm=HuggingFaceEndpoint(repo_id=repo,max_length=128,temperature=0.7,token=tok_id)
print(llm)
# print(llm.invoke('What is langchain_huggingface'))
