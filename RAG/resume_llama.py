from nltk.tokenize import sent_tokenize
from accelerate import disk_offload
import faiss
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class ResumeRAG:
    def __init__(self, resume_text, model_name="meta-llama/Meta-Llama-3.1-8B-Instruct"):
    # def __init__(self, resume_text, model_name="meta-llama/Meta-Llama-3.1-8B"):    
        self.resume_text = resume_text
        self.sentences = sent_tokenize(resume_text)
        self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.sentence_embeddings = self.sentence_model.encode(self.sentences)
        
        # Initialize FAISS index
        self.dimension = self.sentence_embeddings.shape[1]
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(self.sentence_embeddings.astype('float32'))
        
        # Load Llama 2 model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        self.model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, low_cpu_mem_usage = True, trust_remote_code=True).cpu()
        # disk_offload(model=model_name, offload_dir=r'C:\Users\KARAN\llama_offload')

        # Use GPU if available
        # self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.device = torch.device("cpu")

    def get_most_relevant_sections(self, query, k=3):
        # Encode the query
        query_embedding = self.sentence_model.encode([query])[0]
        
        # Search the FAISS index
        distances, indices = self.index.search(query_embedding.reshape(1, -1).astype('float32'), k)
        
        relevant_sections = [self.sentences[i] for i in indices[0]]
        return relevant_sections

    def generate_answer(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_new_tokens=150, temperature=0.7, top_p=0.95, do_sample=True)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def answer_question(self, question):
        relevant_sections = self.get_most_relevant_sections(question)
        context = " ".join(relevant_sections)
        
        prompt = f"""<s>[INST] You are a helpful assistant that answers questions based on the given resume information. Here's the relevant information from the resume:

{context}

Now, please answer the following question:
{question}

Provide a concise and accurate answer based solely on the information given in the resume context. If the information is not available in the context, please state that it cannot be determined from the given information. [/INST]"""

        full_response = self.generate_answer(prompt)
        # Extract the assistant's response
        assistant_response = full_response.split("[/INST]")[-1].strip()
        return assistant_response

# Example usage
resume_text = """
John Doe
Email: john.doe@email.com
Phone: (123) 456-7890

Summary:
Experienced software engineer with 5 years of expertise in Python, Java, and web development.

Work Experience:
Software Engineer, Tech Corp (2018-2023)
- Developed and maintained large-scale web applications
- Led a team of 3 junior developers
- Implemented CI/CD pipelines, improving deployment efficiency by 40%

Education:
Bachelor of Science in Computer Science, University of Technology (2014-2018)

Skills:
Python, Java, JavaScript, SQL, Git, Agile methodologies
"""

rag = ResumeRAG(resume_text)

# Example questions
questions = [
    "What is John's email address?",
    "How many years of experience does John have?",
    "What programming languages does John know?",
    "Where did John go to college?",
    "What was John's role at Tech Corp?"
]

for question in questions:
    print(f"Q: {question}")
    print(f"A: {rag.answer_question(question)}\n")