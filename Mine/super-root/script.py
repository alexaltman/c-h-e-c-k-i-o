def super_root(number):

    E = 0.001
    L = 1
    H = 10

    while True:
        M = (L + H) / 2.0
        superPower = M ** M
        residual = superPower - number

        if abs(residual) < E:
            return M
        elif residual < 0:
            L = M
        else:
            H = M
