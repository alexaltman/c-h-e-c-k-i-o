def checkio(m):

    def neighs(y, x, group):
        for i in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            try:
                if m[y][x] == m[y+i[0]][x+i[1]] and y+i[0] >= 0 and x+i[1] >= 0:
                    if [y+i[0], x+i[1]] not in group:
                        group.append([y+i[0], x+i[1]])
                        group = neighs(y+i[0], x+i[1], group)
            except IndexError:  # went off the far side
                pass
        return group

    mali = {}  # master list
    for y in range(len(m)):
        for x in range(len(m[0])):
            neighbors = neighs(y, x, [[y, x]])
            if m[y][x] != 0:
                if len(neighbors) > mali.setdefault(m[y][x], 0):
                    mali[m[y][x]] = len(neighbors)

    maxgrp = [0, 0]  # size, num
    for num, size in mali.items():
        if size > maxgrp[0]:
            maxgrp = [size, num]
    return maxgrp
