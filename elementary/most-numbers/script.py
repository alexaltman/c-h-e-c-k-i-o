def checkio(*args):

    count = 0
    top = 0
    bottom = 0
    for i in args:
        i = float(i)

        if count == 0:
            count += 1
            top = i
            bottom = i
        else:
            if i > top:
                top = i
            elif i < bottom:
                bottom = i

    return top - bottom
