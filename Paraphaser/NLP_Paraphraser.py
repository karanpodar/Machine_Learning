import spacy
from nltk.corpus import wordnet

# Load spacy model for dependency parsing
nlp = spacy.load("en_core_web_sm")

def paraphrase(input_text):
    doc = nlp(input_text)
    paraphrased_sentences = []
    
    for sent in doc.sents:
        paraphrased_sentence = []
        for token in sent:
            if token.pos_ in ('NOUN', 'VERB', 'ADJ'):
                synonyms = wordnet.synsets(token.text)
                if synonyms:
                    paraphrased_sentence.append(synonyms[0].lemmas()[0].name().replace('_', ' '))
                else:
                    paraphrased_sentence.append(token.text)
            else:
                paraphrased_sentence.append(token.text)

        # Join paraphrased words to form sentence
        paraphrased_sentences.append(" ".join(paraphrased_sentence))
    
    # Join all sentences to form the final paraphrased text
    paraphrased_text = " ".join(paraphrased_sentences)
    
    if len(paraphrased_text.split()) >= 0.8 * len(input_text.split()):
        return paraphrased_text


if __name__ == "__main__":
    
    # Example Input
    input_text = "Artificial Intelligence, a rapidly evolving field at the intersection of computer science, mathematics, and cognitive psychology, encompasses a wide array of technologies and methodologies aimed at creating machines capable of performing tasks that typically require human intelligence, including but not limited to visual perception, speech recognition, decision-making, language translation, and creative expression, which has led to groundbreaking advancements in various sectors such as healthcare, where AI-powered diagnostic tools can analyze medical images with unprecedented accuracy, finance, where algorithmic trading systems can process vast amounts of data to make split-second investment decisions, transportation, where self-driving vehicles promise to revolutionize mobility and reduce accidents, education, where personalized learning platforms can adapt to individual students' needs and learning styles, and scientific research, where AI models can simulate complex systems and accelerate the discovery of new materials and drugs, all while raising important ethical questions about privacy, job displacement, algorithmic bias, and the long-term implications of creating machines that may one day surpass human intelligence in many domains."

    # Generate Paraphrase
    paraphrased_output = paraphrase(input_text)
    print("Paraphrased Output:", paraphrased_output)