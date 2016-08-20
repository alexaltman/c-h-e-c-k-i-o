import re

def checkio(data):
    def mappnt(num):
        if num.isalpha():
            num = ord(num) - 48
        num = int(num)
        return num*2 if num*2 < 10 else int(str(num*2)[0])+int(str(num*2)[1]) #assuming only two digits possible

    data = re.sub(r'\W*_*', '', data)

    allmappnts = []
    for e, i in enumerate(data[::-1]):
        if e % 2 == 0:
            allmappnts.append(mappnt(i))

    mysum = sum(allmappnts)
    for e, i in enumerate(data[::-1]):
        if e % 2 != 0:
            if i.isalpha():
                mysum += (ord(i)-48)
            else:
                mysum += int(i)


    finalchar = 10 - (mysum % 10)
    if str(mysum)[-1] == '0':
        finalchar = 0

    return [str(finalchar), mysum]
