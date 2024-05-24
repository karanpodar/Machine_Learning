from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")
data = loader.load()
print(data)
print('*******************************************')

text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(data)
print(documents)

#There are five levels of text splitting, each with different strategies and considerations. The levels are character splitting, recursive character text splitting, document-specific text splitting, semantic splitting, and agentic splitting.