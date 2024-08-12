"""
To find the unique element in an array without XOR, iterating the array or dictionary
"""

arr = [1, 1, 2, 2, 3, 4, 4]

output = 2 * sum(set(arr)) - sum(arr)

print(sum(set(arr)))
print(sum(arr))
print(output)