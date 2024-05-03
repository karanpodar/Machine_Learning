'''
To find the first missing positive integer in the array
Ex1 - in array [1, 2, 3] the first missing positive integer will be 4
Ex2 - in array [7, 2, 7] the first missing positive integer will be 1
'''

def miss_integer(a):
    # print(len(a)+1)
    for i in range(1, (len(a)+2)):
        if i not in a:
            return i
        
inp1 = [1, 2, 3]
inp2 = [7, 2, 7]

print(miss_integer(inp1))
print(miss_integer(inp2))