'''
To find out the length of last word in the array

arr = 'Hello World'
output = 5
explaination = since world is of 5 bytes

arr = 'I Like python  '
output = 6
explaination = since python is of 6 bytes
'''

def len_last_word(arr):

    input = arr.split(' ')
    output = 0
    
    while output <= 0:
    
        if len(input[-1]) == 0:
            input.pop()
        else:
            output = len(input[-1])

    return output


arr = 'Hello World'
print(len_last_word(arr))

arr = 'I Like python  '
print(len_last_word(arr))