def checkio(n, m):
    myn = str(bin(n))
    mym = str(bin(m))
    myn, mym = myn[2:], mym[2:]

    if len(myn) != len(mym):
        if len(myn) < len(mym):
            dif = len(mym) - len(myn)
            myn = ('0'*dif)+myn
            print(myn)
        else:
            dif = len(myn) - len(mym)
            mym = ('0'*dif)+mym
            print(mym)

    H = ''
    for x, y in zip(myn, mym):
        print(x, y)
        if x == '1' and y == '1':
            H += '0'
        else:
            H += str(int(x) + int(y))

    H_sum = 0
    for x in H:
        H_sum += int(x)
    return H_sum
