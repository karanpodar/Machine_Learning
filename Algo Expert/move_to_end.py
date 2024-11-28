def moveElementToEnd(array, toMove):

    # Write your code here.
    l = 0
    r = len(array) - 1
    array.sort()

    # for i in range(len(array)):
    #     if array[i] == toMove:
    #         l = i
    #     elif
    
    while array[r] > toMove or array[l] < toMove:
        if array[r] == toMove:
            end = r
        else:
            r -= 1
        if array[l] == toMove:
            start = l
        else:
            l += 1
    print(l, r)
    print(array[:l])
    print(array[l:r+1])
    print(array[r+1:])
    array[:] = array[:l] + array[r+1:] + array[l:r+1]
    return array

array = [2, 1, 2, 2, 2, 3, 4, 2]
t = 2
print(moveElementToEnd(array,t))