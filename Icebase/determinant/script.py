def checkio(d):

    if len(d[0]) == 1:
        return d[0][0]
    elif len(d[0]) == 2:
        return d[0][0]*d[1][1] - d[0][1]*d[1][0]
    elif len(d[0]) > 2:
        determinant = 0
        for e, i in enumerate(d[0]):
            tmpmatrix = []
            for row in d[1:]:
                row = row[:] # Need a copy of the mutable list inside list so don't change original
                del row[e]
                tmpmatrix.append(row)

            if e % 2 == 0:
                determinant += i*checkio(tmpmatrix)
            else:
                determinant += -1*i*checkio(tmpmatrix)
        return determinant
