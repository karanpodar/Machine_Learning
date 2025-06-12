from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os

# 1. Setup OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

# 2. Load your documents
loader = TextLoader("sample_docs/your_doc.txt")  # Add your document path here
documents = loader.load()

# 3. Split the documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# 4. Embed documents and store them in a FAISS vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

# 5. Create retriever
retriever = vectorstore.as_retriever()

# 6. Initialize LLM and RetrievalQA chain
llm = OpenAI(temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# 7. Ask a question!
query = "What are the key points from the document?"
response = qa_chain.run(query)

print("Answer:", response)
