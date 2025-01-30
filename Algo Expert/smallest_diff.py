def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    
    currDiff = float('inf')
    
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            absDiff = abs(arrayOne[i] - arrayTwo[j])
            if absDiff < currDiff:
                out = [arrayOne[i], arrayTwo[j]]
                currDiff = absDiff
    return out



def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    idx1 = 0
    idx2 = 0
    currDiff = float('inf')

    while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
        absDiff = abs(arrayOne[idx1] - arrayTwo[idx2])
        if absDiff < currDiff:
            out = [arrayOne[idx1], arrayTwo[idx2]]
            currDiff = absDiff
        if arrayOne[idx1] < arrayTwo[idx2]:
            idx1 += 1
        elif arrayOne[idx1] > arrayTwo[idx2]:
            idx2 += 1
        else:
            return [arrayOne[idx1], arrayTwo[idx2]]
    return out