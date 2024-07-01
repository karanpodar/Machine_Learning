from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.barclaycard.co.uk/personal")
data = loader.load()
# print(data)
print(type(data))