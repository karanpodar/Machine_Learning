def spiralTraverse(array):
    # Write your code here.
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
       
        for i in range(startCol, endCol+1):
            result.append(array[startRow][i])
        for i in range(startRow + 1, endRow + 1):
            result.append(array[i][endCol])
        for i in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            else:
                result.append(array[endRow][i])
        for i in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            else:
                result.append(array[i][startCol])
    
        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1
    
    return result