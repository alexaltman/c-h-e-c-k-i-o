def swapsort(array):

    maxsorts = len(array) * (len(array)-1) / 2
    sorts = 0
    li = list(array)

    def oneswap(li):
        sl = sorted(li)
        for e, (good, unk) in enumerate(zip(sl, li)):
            try:
                if unk > li[e+1]:
                    li[e], li[e+1] = li[e+1], li[e]
                    return li, str(e)+str(e+1) + ','
            except IndexError:                          # if u get to end and it's not max
                if unk < li[e-1]:
                    li[e], li[e-1] = li[e-1], li[e]
                    return li, str(e-1)+str(e) + ','
        return li, ''

    allswaps = ''
    while list(li) != sorted(li):
        li, swap = oneswap(li)
        allswaps += swap
        sorts += 1
        if sorts > maxsorts:
            return ''
    return allswaps.rstrip(',')
