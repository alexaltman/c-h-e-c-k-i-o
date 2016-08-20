from fractions import Fraction
from collections import Counter
METALS = ('gold', 'tin', 'iron', 'copper')

def checkio(alloys):

    # secondary property => g+t+i+c = 1
    c = Counter()
    mys = Fraction()

    for key, value in alloys.items():
        keya, keyb = key.split('-')
        c[keya] += 1
        c[keyb] += 1
        mys += value

    if 3 == len([v for k, v in c.items() if v == 2]):
        for k, v in c.items():
            c[k] -= 2
        mys = mys / Fraction(2, 1)

    for metal in METALS:
        if metal not in list(c.keys()):
            c[metal] = 1
        else:
            c[metal] -= 1

    remaining_var = c.most_common()[0]
    remaining_sum = mys - Fraction(1, 1)

    remaining_sum = remaining_sum / Fraction(abs(remaining_var[1]), 1)

    if remaining_var[0] == 'gold':
        return abs(remaining_sum)
    else:
        frac = alloys.get('gold'+'-'+remaining_var[0])
        if not frac:
            frac = alloys.get(remaining_var[0]+'-'+'gold')

        if frac:
            return abs(frac - remaining_sum)
        else:
            for k, v in alloys.items():
                ka, kb = k.split('-')

                if 'gold' != ka and 'gold' != kb:
                    if remaining_var[0] != ka and remaining_var[0] != kb:
                        return mys - alloys[k]


            frac = alloys.get('gold'+'-'+remaining_var[0])
            if not frac:
                frac = alloys.get(remaining_var[0]+'-'+'gold')
