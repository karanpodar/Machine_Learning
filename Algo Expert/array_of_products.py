def arrayOfProducts(array):
    # Write your code here.
    left = [1 for i in range(len(array))]
    right = [1 for i in range(len(array))]
    output = [1 for i in range(len(array))]
    leftProd = 1
    rightProd = 1
    
    for i in range(len(array)):
        left[i] = leftProd
        leftProd *= array[i]

    for i in reversed(range(len(array))):
        right[i] = rightProd
        rightProd *= array[i]

    for i in range(len(array)):
        output[i] = left[i] * right[i]
    return output