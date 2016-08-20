def checkio(data):

    def abu(num):
        nonlocal mys
        mys += num

    mys = 0
    list(map(abu, data))
    return mys
