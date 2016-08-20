import math

def checkio(a, b, c):
    if (a+b) <= c or (a+c) <= b or (b+c) <= a:
        return [ 0, 0, 0 ]

    try:
        A = math.degrees(math.acos(((b**2) + (c**2) - (a**2)) / (2*b*c)))
        B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c)))
        C = math.degrees(math.acos((a**2 - c**2 + b**2) / (2*a*b)))
    except ValueError:
        return [ 0, 0, 0 ]

    tot = round(A) + round(B) + round(C)
    A = round(A)
    B = round(B)
    C = round(C)

    if (A + B + C) != 180:
        return [ 0, 0, 0 ]
    return sorted([A, B, C])
