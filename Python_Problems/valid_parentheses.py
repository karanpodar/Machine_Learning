'''
Given an expression string exp, write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given expression.
Input: exp = “[()]{}{[()()]()}” 
Output: Balanced
Explanation: all the brackets are well-formed

Input: exp = “[(])” 
Output: Not Balanced 
Explanation: 1 and 4 brackets are not balanced because 
there is a closing ‘]’ before the closing ‘(‘
'''

def check_valid(exp):

    brackets = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
                }
    
    output = []

    for i in range(len(exp)):

        if exp[i] in brackets:
            
            if output[-1] == brackets[exp[i]]:
                output.pop()

        else:
            output.append(exp[i])

    return output
            
def check_valid_replace(exp):

    for i in range((len(exp)//2)+1):

        exp = exp.replace('{}', '')
        exp = exp.replace('[]', '')
        exp = exp.replace('()', '')

    return exp


exp = '[()]{}{[()()]()}'
print(check_valid_replace(exp))
print(check_valid(exp))
print(exp)

if any(check_valid(exp)):
    print('Un-Balanced')
else:
    print('Balanced')

exp = '[(])'
print(check_valid_replace(exp))
print(check_valid(exp))
print(exp)

if any(check_valid_replace(exp)):
    print('Un-Balanced')
else:
    print('Balanced')