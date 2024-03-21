from nltk.corpus import stopwords
import nltk

def __remove_stopwords(text):
    """
    Takes a String
    return List
    """
    words= []
    for x in text.split():

        if x.lower() in stopwords.words('english'):
            pass
        else:
            words.append(x)
    return words

