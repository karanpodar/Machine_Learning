import string

def __remove_punctuation(text):
    """
    Takes a String
    return : Return a String
    """
    message = []
    for x in text:
        if x in string.punctuation:
            pass
        else:
            message.append(x)
    message = ''.join(message)

    return message