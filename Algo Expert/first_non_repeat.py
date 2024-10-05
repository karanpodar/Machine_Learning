strings = "abacfe"

def firstNonRepeatingCharacter(string):
    # Write your code here.
    for i,v in enumerate(string):
        if string.count(v) > 1:
            continue
        else:
            return i
    return -1

print(firstNonRepeatingCharacter(strings))