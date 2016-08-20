def checkio(p, i):

    def check_patt(i_r, i_c):
        for e, r in enumerate(p):
            for e2, c in enumerate(r):
                try:
                    if i[i_r+e][i_c+e2] != c:
                        return False
                except IndexError:
                    return False
        return True

    def change_patt(i_r, i_c):
        for e, r in enumerate(p):
            for e2, c in enumerate(r):
                if i[i_r+e][i_c+e2] == 0:
                    i[i_r+e][i_c+e2] = 2
                else:
                    i[i_r+e][i_c+e2] = 3

    for w in range(len(i)):
        switch = False
        for v in range(len(i[w])):
            switch = check_patt(w, v)
            if switch:
                change_patt(w, v)
    return i
