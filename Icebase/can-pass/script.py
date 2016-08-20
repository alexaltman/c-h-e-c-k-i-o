def can_pass(grid, start, end):

    pathval = grid[start[0]][start[1]]

    def getpath(start, thepath):
        coords = [(x+start[0], y+start[1]) for x, y in [[1, 0], [-1, 0], [0, -1], [0, 1]]]
        for coord in coords:
            try:
                if coord[0] >= 0 and coord[1] >= 0 and grid[coord[0]][coord[1]] == pathval:
                    if coord not in thepath:
                        thepath.append(coord)
                        thepath = getpath(coord, thepath)
            except IndexError:
                continue
        return thepath

    thepath = getpath(start, [start])

    if start in thepath and end in thepath:
        return True
    return False
