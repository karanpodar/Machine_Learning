from nltk.tokenize import sent_tokenize
import faiss
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class ResumeRAG:
    def __init__(self, resume_text, model_name="google/flan-t5-small"):
    # def __init__(self, resume_text, model_name="meta-llama/Meta-Llama-3.1-8B-Instruct"):
        self.resume_text = resume_text
        self.sentences = sent_tokenize(resume_text)
        self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.sentence_embeddings = self.sentence_model.encode(self.sentences)
        
        # Initialize FAISS index
        self.dimension = self.sentence_embeddings.shape[1]
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(self.sentence_embeddings.astype('float32'))
        
        # Load Hugging Face model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        
        # Use GPU if available
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def get_most_relevant_sections(self, query, k=3):
        # Encode the query
        query_embedding = self.sentence_model.encode([query])[0]
        
        # Search the FAISS index
        distances, indices = self.index.search(query_embedding.reshape(1, -1).astype('float32'), k)
        
        relevant_sections = [self.sentences[i] for i in indices[0]]
        return relevant_sections

    def generate_answer(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True).to(self.device)
        outputs = self.model.generate(**inputs, max_length=150, num_return_sequences=1, temperature=0.7)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def answer_question(self, question):
        relevant_sections = self.get_most_relevant_sections(question)
        context = " ".join(relevant_sections)
        
        prompt = f"""Based on the following resume information:

{context}

Answer the following question:
{question}

Provide a concise and accurate answer based solely on the information given in the resume context. If the information is not available in the context, please state that it cannot be determined from the given information."""

        answer = self.generate_answer(prompt)
        return answer

with open(r'RAG\resume.txt', 'r', encoding="utf8") as f1:
    resume_text = f1.read()

rag = ResumeRAG(resume_text)

# Example questions
questions = [
    "What is karan's email address?",
    "How many years of experience does karan have?",
    "What programming languages does karan know?",
    "Where did karan go to college?",
    "What was karan's role at Tech Corp?"
]

for question in questions:
    print(f"Q: {question}")
    print(f"A: {rag.answer_question(question)}\n")