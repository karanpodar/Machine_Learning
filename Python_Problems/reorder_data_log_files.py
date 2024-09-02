'''
Reorder Data in Log Files

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

Example 2:

Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
'''


def reorder_data(arr):
    
    output = []
    letter_log = {}
    digit_log = []

    for i in arr:
        
        identifier = i.split(' ', 1)
        
        if identifier[1].replace(' ', '').isnumeric():
            digit_log.append(i)
        else:
            print(identifier[1])
            if identifier[1] in letter_log:
                letter_log[identifier[1]].append(identifier[0])
            else:
                letter_log[identifier[1]] = []
                letter_log[identifier[1]].append(identifier[0])


    for key, values in sorted(letter_log.items()):

        if len(values) > 1:
            for value in sorted(values):
                output.append(value + ' ' + key)
        else:
                output.append(values[0] + ' ' + key)

    return output + digit_log


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorder_data(logs))

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(reorder_data(logs))

logs = ["a2 act car","g1 act car","a2 act car1","g1 act car1"]
print(reorder_data(logs))