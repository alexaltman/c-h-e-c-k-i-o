def checkio(matrix):
    if len(matrix) == 0:
        return False
    elif len(matrix) < 4:
        if len(matrix[0]) < 4:
            return False
        else:
            return search_axis(matrix)

    #search x, y, diag.
    xbool = search_axis(matrix)
    if xbool: return True
    ybool = search_axis(zip(*matrix))
    if ybool: return True
    diagbool = search_diag(matrix)
    return diagbool

def search_diag(matrix):
    #x+1, y+1  OR  x-1, y-1
    for y, i in enumerate(matrix):
        for x, i2 in enumerate(i):
            NW_SE = [] #aka walk L to R over x axis
            try:
                NW_SE.append(matrix[y][x])
                NW_SE.append(matrix[y+1][x+1])
                NW_SE.append(matrix[y+2][x+2])
                NW_SE.append(matrix[y+3][x+3])
                if len(set(NW_SE)) <= 1:
                    return True
            except IndexError:
                continue
        for x, i2 in reversed(list(enumerate(i))):
            NE_SW = [] #aka walk R to L over x axis
            try:
                if x < 3:
                    continue
                NE_SW.append(matrix[y][x])
                NE_SW.append(matrix[y+1][x-1])
                NE_SW.append(matrix[y+2][x-2])
                NE_SW.append(matrix[y+3][x-3])
                if len(set(NE_SW)) <= 1:
                    return True
            except IndexError:
                continue
    return False

def search_axis(matrix):
    '''Defaults to searching x axis (L-R)'''
    myi = ''
    count = 0
    for i in matrix:
        count = 0
        for x in i:
            if not myi:
                myi = x
                count += 1
                continue

            if myi == x:
                count += 1
                if count >= 4:
                    return True
            else:
                myi = x
                count = 1
    return False
