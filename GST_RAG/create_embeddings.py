from sentence_transformers import SentenceTransformer
from chunking import extract_text_from_pdf, split_text
import faiss
import pickle

# Create embeddings for each chunk and store them in a ChromaDB
def create_vector_db(text_chunks):
    
    embeddings = SentenceTransformer("all-MiniLM-L6-v2")
    chunk_embeddings = embeddings.encode(text_chunks)
    
    dimension = chunk_embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(dimension)
    faiss_index.add(chunk_embeddings)
    
    # print(faiss_index.ntotal)
    faiss.write_index(faiss_index, './GST_RAG/faiss_index.bin')

    with open('./GST_RAG/faiss_chunks.pkl', 'wb') as f:
        pickle.dump(text_chunks, f)

    return None


pdf_path = r"GST_RAG\66_GST_Smart_Guide.pdf"
document_text = extract_text_from_pdf(pdf_path)
text_chunks = split_text(document_text)
create_vector_db(text_chunks)