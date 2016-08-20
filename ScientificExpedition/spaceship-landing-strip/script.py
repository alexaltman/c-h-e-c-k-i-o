from itertools import groupby

def checkio(m):
    mymax = 0

    n = []
    for row in m:
        tmp = []
        for i in row:
            if any(i == x for x in 'GS'):
                tmp.append(1)
            else:
                tmp.append(-20) # somewhat arbitrary -20, once a cell goes neg it should stay neg
        n.append(tmp)

    # find longest single row - L to R
    for row in n:
        for k, g in groupby(row, key=lambda x: x == 1):
            if k:
                le = len(list(z for z in g))
                mymax = max(mymax, le)

    # Transpose rows upwards
    for e, row in enumerate(n):
        if e != 0:                   # don't try to grab a neg indexed row
            tmprow = []              # Stores aggreg sum values of entire run
            lists = [row]            #Accumulate the lists as we walk "upwards" in the m towards the starting row

            for r2 in reversed(n[:e]):
                lists.append(r2)
                tmprow = map(sum, zip(*lists))

                # sum adjacent pos.s
                count = 0
                for i in tmprow:
                    if i > 0:
                        count += i
                        # check against mymax and set if >
                        mymax = max(count, mymax)
                    else:
                        count = 0

    return mymax
