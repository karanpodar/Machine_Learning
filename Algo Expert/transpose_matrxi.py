def transposeMatrix(matrix):
    # Write your code here.
    output = [[] for _ in range(len(matrix[0]))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                output[i].insert(j, matrix[i][j])
            else:
                output[j].insert(i, matrix[i][j])
    return output
