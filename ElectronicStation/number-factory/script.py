def checkio(x):
    myf = myfactors(x)
    myf = convert_twosandfours(myf)
    myf.sort()
    if len(str(myf[-1])) > 1: return 0
    final = ''.join([str(x) for x in myf])
    if int(final) == x:
        return 0
    return int(final)

def convert_twosandfours(myl):

    while myl.count(2) >= 3:
        myl.remove(2)
        myl.remove(2)
        myl.remove(2)
        myl.append(8)
    while myl.count(3) >= 2:
        myl.remove(3)
        myl.remove(3)
        myl.append(9)
    while myl.count(2) >= 1 and myl.count(3) >= 1:
        myl.remove(2)
        myl.remove(3)
        myl.append(6)
    while myl.count(2) >= 2:
        myl.remove(2)
        myl.remove(2)
        myl.append(4)
    return myl

def myfactors(x):
    fac = []
    n = 2
    while n*n <= x:
        while (x % n) == 0:
            fac.append(n)
            x //= n
        n += 1
    if x > 1:
       fac.append(x)
    return fac
