def checkio(opacity):
    print('starting')
    return getage(opacity)


def isfibo(number):
    n, prev, two_prev = 1, 0, 0

    while number >= n:
        prev, two_prev = n, prev
        n = prev + two_prev
        if number == n:
            return True
    return False

def getage(opacity):
    beg_opacity = 10000
    age = 0
    while opacity != beg_opacity:
        age += 1
        print(age)
        if isfibo(age):
            beg_opacity -= age
            print(age, beg_opacity)
        else:
            beg_opacity += 1
    return age
