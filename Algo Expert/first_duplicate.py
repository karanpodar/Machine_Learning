def firstDuplicateValue(array):
    # Write your code here.
    passed = set()

    for i in array:
        if i in passed:
            return i
        else:
            passed.add(i)
    return -1


def firstDuplicateValue(array):
    # Write your code here.
    for i in array:
        index = abs(i) - 1
        if array[index] < 0:
            return abs(i)
        else:
            array[index] = -array[index]
    return -1