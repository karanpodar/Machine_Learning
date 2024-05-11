""" 
Subarray of an array

Ex1 - arr1 = [10, 5, 2, 6] then output should have all the subarrays possible [10], [10, 5], [5] ...... 
"""

arr1 = [10, 5, 2, 6, 5]

def subarry(arr1):
    
    output = []
    
    for i in range(0, len(arr1)):
      
        for j in range(i, len(arr1)):

            output.append(arr1[i:j+1])

    return output

print(subarry(arr1))
