import fractions as fr

def divide_pie(groups):
    ndrones = sum([abs(i) for i in groups])
    pieleft = fr.Fraction(ndrones, ndrones)

    for i in groups:
        if i < 0:
            pieleft *= fr.Fraction(ndrones - abs(i), ndrones)
        else:
            pieleft -= fr.Fraction(i, ndrones)

    return pieleft.numerator, pieleft.denominator
