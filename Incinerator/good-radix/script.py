def checkio(n):

    for radix in range(1, 37):
        try:
            num = int(n, radix)
        except ValueError:
            continue

        if num % (radix-1) == 0:
            return radix

    return 0
