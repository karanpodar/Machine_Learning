def nextGreaterElement(array):
    # Write your code here.
    hold = array
    hold.sort()

    for i in range(len(array)-1):
        for j in range(len(hold)-1):
            if hold[j] > array[i]:
                array[i] = hold[j]
                hold[j] = float('-inf')
                break
            # array[i] = -1
        
    return array

array= [0, 1, 2, 3, 4]
# print(nextGreaterElement(array))
print(8%8)

