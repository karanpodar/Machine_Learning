'''
To find the common occurence of elements in 2 array at an index(0 indexed)

Input: A = [1,3,2,4], B [3,1,2,4] Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[o] = 0.
Ati=1:1 and 3 are common in A and B, so C[1] = 2.
At = 2:1,2, and 3 are common in A and B, so C[2] = 3.
At =3: 1,2, 3, and 4 are common in A and B, so C[3] = 4.

Example 2:
Input: A = [2,3,1], B [3,1,2] Output: [0,1,3]
Explanation: At i = 0: no number is common, so C[o] = 0.
At i= 1: only 3 is common in A and B, so C[1] = 1.
At i= 2:1, 2, and 3 are common in A and B, so C[2] = 3.
'''

def common_element(arr, arr1):

    output = []
    count = 0

    for i in range(len(arr)):
        
        count = 0
        j = 0

        while j < i+1:

            if arr[j] in arr1[:i+1]:
                count += 1
            j += 1
            
        output.append(count)
    
    return output

A = [6,1,3,2,4]
B = [6,3,1,2,4]

print(common_element(A, B))

A = [2,3,1]
B = [3,1,2] 

print(common_element(A, B))