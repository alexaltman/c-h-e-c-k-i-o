def total_cost(calls):
    ducats = 0
    da1_last = ''
    tot_mymin = 0
    da1 = ''
    for i in calls:
        da1, da2, dur = i.split(" ")
        y, m, d = da1.split('-')
        if not da1_last: da1_last = da1

        mymin = int(int(dur) / 60)
        if int(dur) % 60 > 0:
            mymin += 1

        if da1 not in da1_last:
            tot_mymin = 0

        tot_mymin += mymin

        if tot_mymin <= 100:
            ducats += mymin
        if tot_mymin > 100:
            if tot_mymin - mymin > 100:
                ducats += 2 * mymin
            else:
                oldadd = (tot_mymin - mymin)
                x = 100 - oldadd
                ducats += x
                ducats += (mymin - x) *2
        da1_last = da1
    return ducats
