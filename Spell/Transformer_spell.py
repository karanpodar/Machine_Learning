import re
import string
from nltk.corpus import words
from nltk.metrics.distance import edit_distance
from transformers import pipeline
import nltk
import warnings
warnings.filterwarnings("ignore")

print(__name__)
# Download the word list for NLTK
# nltk.download('words')
word_list = words.words()

# Preprocess the text: lowercase and remove punctuation
def preprocess(text):
    text = text.lower()
    text = re.sub(f'[{string.punctuation}]', '', text)
    return text.split()

# Generate spelling correction candidates using edit distance
def generate_candidates(word, max_distance=2):
    candidates = [w for w in word_list if edit_distance(w, word) <= max_distance]
    return candidates

# Load pre-trained language model for contextual understanding
fill_mask = pipeline('fill-mask', model='Davlan/xlm-roberta-base-finetuned-english')

# Get the best candidate correction based on context
def get_best_candidate(context, word, candidates):
    print(context)
#    masked_sentence = context.replace(word, '[MASK]')
    
#    predictions = fill_mask(masked_sentence)
    predictions = fill_mask(context)
    candidates_scores = {candidate: 0 for candidate in candidates}
    #print('predictions', predictions)
    for prediction in predictions:
        print(prediction)
        token = prediction['token_str']
        if token in candidates_scores:
            candidates_scores[token] = prediction['score']
    best_candidate = max(candidates_scores, key=candidates_scores.get)
    return best_candidate

# Correct the entire sentence
def correct_sentence(sentence):
    words = preprocess(sentence)
    corrected_sentence = []
    for i, word in enumerate(words):
        candidates = generate_candidates(word)
        if not candidates:
            corrected_sentence.append(word)
            continue
        context = ' '.join(words[:i] + ['[MASK]'] + words[i+1:])
        best_candidate = get_best_candidate(context, word, candidates)
        corrected_sentence.append(best_candidate)
    return ' '.join(corrected_sentence)

# Example usage
if __name__ == "__main__":
    sentence = "I havv a sppeling erorr."
    corrected = correct_sentence(sentence)
    print(f"Original: {sentence}")
    print(f"Corrected: {corrected}")