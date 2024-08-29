""" 
Subarray Product less than k
To find a subarray in which the product of elements is less than k

Ex1 - arr1 = [10, 5, 2, 6], k = 100 then output should be [10], [10, 5], [5] ...... 
"""

arr1 = [10, 5, 2, 6]
k = 100 

def subarry_prod(arr1, k):
    
    output = []
    
    for i in range(0, len(arr1)):
        prod = 1
        for j in range(i, len(arr1)):
            prod = prod * arr1[j]

            if prod < k:
            # if prod_array(arr1[i:j+1]) < k:
                output.append(arr1[i:j+1])

    return output

def prod_array(arr):

    prod = 1
    
    for i in arr:
        prod = i * prod
    
    return prod

print(subarry_prod(arr1, k))