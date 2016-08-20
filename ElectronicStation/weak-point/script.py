def weak_point(matrix):
    # index, sum
    lowest_r = [ ]
    lowest_c = [ ]

    def get_sum(matrix, vec='r'):
        nonlocal lowest_r, lowest_c
        for e, i in enumerate(matrix):
            if vec == 'r':
                try:
                    if sum(i) < lowest_r[1]:
                        lowest_r[0] = e
                        lowest_r[1] = sum(i)
                except:
                    lowest_r.append(e)
                    lowest_r.append(sum(i))
            if vec == 'c':
                try:
                    if sum(i) < lowest_c[1]:
                        lowest_c[0] = e
                        lowest_c[1] = sum(i)
                except:
                    lowest_c.append(e)
                    lowest_c.append(sum(i))

    get_sum(matrix, vec='r')
    new_matrix = zip(*matrix)
    get_sum(new_matrix, vec='c')
    return (lowest_r[0], lowest_c[0])
