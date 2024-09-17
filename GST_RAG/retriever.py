from sentence_transformers import SentenceTransformer
import faiss
import pickle

def load_faiss_indices(query):
    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = embedding_model.encode([query])
    new_vector_store = faiss.read_index('./GST_RAG/faiss_index.bin')
    # print(new_vector_store.ntotal)

    D, I = new_vector_store.search(query_embedding, k=3)
    result = fetch_chunks(I)
    
    return result


def fetch_chunks(I):

    # print(I)
    with open('./GST_RAG/faiss_chunks.pkl', 'rb') as f1:
        text_chunks = pickle.load(f1)
        # print(f1)
    
    result = [text_chunks[i] for i in I[0]]

    return '/n'.join(result)


# Example query
if __name__ == "__main__":
    query = "About the Author"
    answer = load_faiss_indices(query)
    print(answer)