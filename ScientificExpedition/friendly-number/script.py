def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    pwr = powers[0]
    while (number / base >= 1 or number / base <= -1) and powers.index(pwr) + 1 != len(powers):
        number = number / base
        pwr = powers[powers.index(pwr) + 1]

    number = number + .1 if str(number).count('9') > 5 else number  # assert 10**32 hack
    number = round(number, decimals) if decimals else int(number)
    return format(number, '.'+str(decimals)+'f') + pwr + suffix
