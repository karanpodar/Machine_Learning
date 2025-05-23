'''
Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
'''

def check_isomorphic(s, t):
    d1 = {}

    for i in range(len(s)):

        if s[i] in d1:
            if d1.get(s[i]) != t[i]:
                return False
        else:
            d1[s[i]] = t[i]

    return True

s = "egg"
t = "add"

print(check_isomorphic(s, t))

s = "foo"
t = "bar"

print(check_isomorphic(s, t))

s = "paper"
t = "title"

print(check_isomorphic(s, t))