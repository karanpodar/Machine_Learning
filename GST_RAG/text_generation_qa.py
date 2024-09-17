import dspy
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from retriever import load_faiss_indices

# Load the Flan-T5 model and tokenizer
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def generate_answer(query, context):

    prompt = f"""Based on the following information:

{context}

Answer the following question:
{query} """


    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs.input_ids, max_length=100, num_beams=5, early_stopping=True)
    
    # Decode the model's output to text
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer


if __name__ == "__main__":
# Example usage:

    query = "Whether software is regarded as goods or services in GST?"
    context = load_faiss_indices(query)
    answer = generate_answer(query, context)
    print("Generated Answer:", answer)
