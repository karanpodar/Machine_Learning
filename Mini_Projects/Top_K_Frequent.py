'''
Given an array of N numbers and a positive integer K. 
The problem is to find K numbers with the most occurrences, i.e., 
the top K numbers having the maximum frequency.
The numbers should be displayed in decreasing order of their frequencies. 
It is assumed that the array consists of at least K numbers.
Input: arr[] = {3, 1, 4, 4, 5, 2, 6, 1}, K = 2
Output: 4 1
'''

def k_frequent(arr, k):
    d = {}
    
    for i in arr:
        if i in d:
            d[i] += 1
            
        else:
            d[i] = 1
    
    output = sorted(d, key=lambda x: d[x])

    output = output[len(output)-k:len(output)]

    return output

arr = [3, 1, 5, 2, 7, 7, 4, 4]
K = 3

print(k_frequent(arr, K))