"""
String reverse using Stack
"""
from collections import deque 

a = 'Hello'
stack = deque(a)
s = []

for i in range(len(a)): 
    s.append(stack.pop())
    output = ''.join(s)

print(output)