import math


def checkio(r):
    tiles = 0
    partials = 0
    radiusSq = r**2

    for r in range(math.ceil(r)):
        for c in range(math.ceil(math.sqrt(radiusSq - r ** 2))):
            if r ** 2 + c ** 2 < radiusSq:
                if (r + 1) ** 2 + (c + 1) ** 2 <= radiusSq:
                    tiles += 1
                else:
                    partials += 1

    return [tiles*4, partials*4]
