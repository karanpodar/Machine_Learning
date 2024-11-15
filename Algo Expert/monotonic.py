def isMonotonic(array):
    # Write your code here.
    a = sorted(array)
    b = sorted(array, reverse=True)

    if array == a or array == b:
        return True

    return False
    

def isMonotonic(array):
    # Write your code here.
    isInc = False
    isDec = False

    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            isDec = True
        if array[i] > array[i-1]:
            isInc = True

    if isInc and isDec:
        return False
    return True
