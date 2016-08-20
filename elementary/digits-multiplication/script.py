def checkio(number):
    number = str(number)
    bignum = 1
    for i in number:
        if i == "0":
            continue
        else:
            bignum *= int(i)
    return bignum
