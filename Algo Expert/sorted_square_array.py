def sortedSquaredArray(array):
    # Write your code here.
    start = 0
    end = len(array) - 1
    output = [0 for _ in array]
    
    for idx in reversed(range(len(array))):
        startval = array[start] * array[start]
        endval = array[end] * array[end]
        if startval < endval:
            output[idx] = endval
            end -= 1
        else:
            output[idx] = startval
            start += 1
    return output
            