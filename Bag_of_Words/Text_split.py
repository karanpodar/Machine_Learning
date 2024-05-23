from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")
data = loader.load()
print(data)
print('*******************************************')
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(data)
print(documents)