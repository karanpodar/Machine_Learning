def findThreeLargestNumbers(array):
    # Write your code here.
    large = [float('-inf')] * 3

    for i in array:
        if large[2] < i:
            large.pop(0)
            large.insert(2, i)
            
        elif large[1] < i:
            large.pop(0)
            large.insert(1, i)
            
        elif large[0] < i:
            large.pop(0)
            large.insert(0, i)

    return large
            
# def large_update(large, num, idx):
#     for i range(idx + 1):
#         if i == idx:
        
array= [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(array))