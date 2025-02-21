def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    out = []

    for x in range(len(array)):
        
        y = x + 1
        z = len(array) - 1
        
        while y < z:
            currentSum = array[x] + array[y] + array[z]
         
            if currentSum == targetSum:
                out.append([array[x], array[y], array[z]])
                y += 1
                z -= 1
            elif currentSum < targetSum:
                y += 1 
            else:
                z -= 1
    return out

array = [1,2,3,4,6]
t = 6
print(threeNumberSum(array, t))

array = [12, 3, 1, 2, -6, 5, -8, 6]
t = 0
print(threeNumberSum(array, t))