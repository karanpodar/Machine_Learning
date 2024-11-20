def semordnilap(words):
    # Write your code here.
    output = []
    paired = []
    for i in words:
        if i not in paired:
            reverse = i[::-1] 
            if reverse in words and reverse != i:
                paired.append(reverse)
                output.append([i, reverse]) 
    return output
