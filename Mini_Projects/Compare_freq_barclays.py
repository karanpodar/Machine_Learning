'''
Check if the input character and document has same frequency of elements
'''


def create_dict(arr):

    dict1 = {}
    for i in arr:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    # print(dict1)
    return dict1

def check_valid(char, doc):

    char_dict = create_dict(char)
    doc_dict = create_dict(doc)

    for key in doc_dict:
        if key not in char_dict:
            return False
        else:
            if char_dict[key] != doc_dict[key]:
                return False

    return True 

char = 'ybrcalass'
doc = 'barclayss'

print(create_dict(char))
print(create_dict(doc))
print(check_valid(char, doc))

char = 'ybrcalass'
doc = 'barclays'

print(create_dict(char))
print(create_dict(doc))
print(check_valid(char, doc))

char = 'ybrcalas'
doc = 'barclayss'

print(create_dict(char))
print(create_dict(doc))
print(check_valid(char, doc))