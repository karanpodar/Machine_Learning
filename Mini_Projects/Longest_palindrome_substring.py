'''
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''

def longest_palindrome(arr):
    output = ''
    if len(arr) < 2:
        return arr
    for i in range(len(arr)):
        if len(arr[i:]) > len(output):
            for j in range(i+1, len(arr)+1):
                if arr[i:j] == arr[i:j][::-1]:
                    if len(output) < len(arr[i:j]):
                        output = arr[i:j]

    return output   

s = "babad"
print(longest_palindrome(s))

s = "bb"
print(longest_palindrome(s))

s= 'a'
print(longest_palindrome(s))

s= 'abcdbbfcba'
print(longest_palindrome(s))