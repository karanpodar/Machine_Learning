from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def paraphrase(
    question,
    text_length,
    num_beams=2,
    num_beam_groups=2,
    num_return_sequences=1,
    repetition_penalty=10.0,
    diversity_penalty=3.0,
    no_repeat_ngram_size=2,
    temperature=0.5,
    model="humarin/chatgpt_paraphraser_on_T5_base"
):
    
    tokenizer = AutoTokenizer.from_pretrained(model)
    model = AutoModelForSeq2SeqLM.from_pretrained(model)

    input_ids = tokenizer(
        f'paraphrase: {question}',
        return_tensors="pt", padding="longest",
        truncation=True,
        max_length=400
    ).input_ids
    
    outputs = model.generate(
        input_ids, temperature=temperature, repetition_penalty=repetition_penalty,
        num_return_sequences=num_return_sequences, no_repeat_ngram_size=no_repeat_ngram_size,
        num_beams=num_beams, num_beam_groups=num_beam_groups,
        diversity_penalty=diversity_penalty,
        max_length=int(3 * text_length)
        # min_length=int(0.8 * text_length)
    )

    res = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return res


if __name__ == "__main__":
   
    original_text = "Artificial Intelligence, a rapidly evolving field at the intersection of computer science, mathematics, and cognitive psychology, encompasses a wide array of technologies and methodologies aimed at creating machines capable of performing tasks that typically require human intelligence, including but not limited to visual perception, speech recognition, decision-making, language translation, and creative expression, which has led to groundbreaking advancements in various sectors such as healthcare, where AI-powered diagnostic tools can analyze medical images with unprecedented accuracy, finance, where algorithmic trading systems can process vast amounts of data to make split-second investment decisions, transportation, where self-driving vehicles promise to revolutionize mobility and reduce accidents, education, where personalized learning platforms can adapt to individual students' needs and learning styles, and scientific research, where AI models can simulate complex systems and accelerate the discovery of new materials and drugs, all while raising important ethical questions about privacy, job displacement, algorithmic bias, and the long-term implications of creating machines that may one day surpass human intelligence in many domains."
    print("Original text:")
    print(original_text)
    print("\nParaphrased versions:")
    text_length = len(original_text)
    paraphrases = paraphrase(original_text, text_length)

    for i, paraphrase in enumerate(paraphrases, 1):
            print(f"{i}. {paraphrase}")