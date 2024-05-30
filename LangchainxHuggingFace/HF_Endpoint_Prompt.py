import os
from langchain_huggingface import HuggingFaceEndpoint
# from langchain_community.llms import HuggingFaceEndpoint
import transformers
from langchain import PromptTemplate, LLMChain

# HF_TOKEN = os.getenv('HF_TOKEN')
os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv('HUGGINGFACEHUB')
tok_id = os.environ['HUGGINGFACEHUB_API_TOKEN']

repo="meta-llama/Llama-2-7b-hf"
llm=HuggingFaceEndpoint(repo_id=repo,max_length=128,temperature=0.7,token=tok_id)
print(llm)

question="Who won the Cricket World Cup in the year 2011?"
template = """Question: {question}
Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])
print(prompt)

llm_chain=LLMChain(llm=llm,prompt=prompt)
print(llm_chain.invoke(question))