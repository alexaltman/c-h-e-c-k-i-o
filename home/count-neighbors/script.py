def count_neighbours(grid, row, col):


    # How to shift coord.s to address neighbors
    shift_list = [[-1, -1],
                  [0, -1],
                  [1, -1],
                  [1, 0],
                  [1, 1],
                  [0, 1],
                  [-1, 1],
                  [-1, 0]]

    rowcol = [row, col]

    # create coordinate list from orig row/col shifted
    # according to shift_list
    coord_list = []
    for i in shift_list:
        new_row = row + i[0]
        new_col = col + i[1]
        if new_row < 0 or new_col < 0:
            continue
        coord_list.append([new_row, new_col])

    print(coord_list)
    da_count = 0
    #address the coordinates to determine if grid has 1/0
    for i in coord_list:
        try:
            if grid[i[0]][i[1]] == 1:
                da_count += 1
        except IndexError:
            print('oor: ' + str(i[0]), str(i[1]))
            next

    return da_count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"

