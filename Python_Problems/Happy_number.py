'''
Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
'''

def happy_number(n):

    s = set()
    
    while n != 1:
        
        if n in s: 
            return False
        s.add(n)
        n = sum([int(i) ** 2 for i in str(n)])

    return True

num = 2

print(happy_number(num))

num = 19

print(happy_number(num))