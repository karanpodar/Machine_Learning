x = 123

def reverse_int(x):
    output = 0
    while x != 0:

        temp = x % 10
        output = output*10 + temp
        x = x // 10
        
    return output

print(reverse_int(x))