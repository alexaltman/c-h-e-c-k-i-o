def checkio(matrix):
    ylen = len(matrix)
    xlen = len(matrix[0])
    #Capture the middle of the matrix the hard way
    for i in range(ylen):
        if matrix[0][0] != matrix[i][i]:
            return False
    #Everything else
    for e, y in enumerate(matrix):
        for e2, x in enumerate(y):
            if matrix[e2][e] != (-1 * matrix[e][e2]):
                return False
    return True
