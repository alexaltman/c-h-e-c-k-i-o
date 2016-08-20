def checkio(matrix):

    if len(matrix[0]) < 1:
        return matrix
    elif len(matrix[0]) == 1:
        mylist = []
        for sm_li in matrix:
            for i in sm_li:
                mylist.append(i)
        return [mylist]

    xcount = 0
    ycount = 0
    for y in matrix:
        ycount += 1
        if not xcount:
            for x in y:
                xcount += 1

    return list(zip(*matrix))
    new_matrix = []
    for e in enumerate(matrix[0]):
        new_matrix.append([])

    for e, li in enumerate(matrix):
        for e, i in enumerate(li):
            new_matrix[e].append(0)

    for e, y in enumerate(matrix):
        for e2, x in enumerate(y):
            new_matrix[e2][e] = x

    return new_matrix
