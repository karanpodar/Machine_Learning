def generateDocument(characters, document):
    # Write your code here.
    if len(document) > len(characters):
        return False
    else:
        counted = set()

        for i in document:
            if i in counted:
                continue
            else:
                counted.add(i)
                if characters.count(i) >= document.count(i):
                    continue
                else:
                    return False
        
    return True
