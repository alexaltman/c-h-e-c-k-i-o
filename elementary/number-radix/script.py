import string

def checkio(str_number, radix):
    tot = 0
    position = 0
    for i in reversed(str_number):
        print(i)
        value = validate(i, position, radix)
        if value == False:
            return -1

        tot += conv(i, position, radix)
        position += 1

    return tot

def conv(digit, position, radix):
    if digit.isalpha():
        digit = alphabet_conv(digit.lower())

    digit = (int(digit) * (radix ** position))
    return digit

def validate(digit, position, radix):
    if digit.isalpha():
        digit = alphabet_conv(digit.lower())
    print(digit, radix)
    if (int(digit)) >= radix:
        return False
    else:
        return True

def alphabet_conv(alpha_dig):
    alpha_conv = string.ascii_lowercase.index(alpha_dig) + 10
    return alpha_conv
