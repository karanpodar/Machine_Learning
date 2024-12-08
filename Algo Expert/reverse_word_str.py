def reverseWordsInString(string):
    # Write your code here.
    out = []
    
    left = 0
    right = 0
    white = False
    
    while right < len(string):
        if white:
            if string[right] != ' ':
                out.insert(0, string[left:right])
                left = right
                white = False
        else:
            if string[right] == ' ':
                out.insert(0, string[left:right])
                left = right
                white = True
        right += 1
    out.insert(0, string[left:])
    return ''.join(out)
