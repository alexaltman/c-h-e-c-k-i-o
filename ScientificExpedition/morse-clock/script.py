def checkio(t_str):
    t_li = t_str.split(':')
    t_li = [i.zfill(2) for i in t_li]

    morse = ''
    for e, i in enumerate(t_li):
        a = i[0]
        b = i[1]

        if e == 0:
            morse += str(bin(int(a)))[2:].zfill(2)
            morse += ' '
            morse += str(bin(int(b)))[2:].zfill(4)
            morse += ' '
            morse += ':'
        else:
            morse += ' '
            morse += str(bin(int(a)))[2:].zfill(3)
            morse += ' '
            morse += str(bin(int(b)))[2:].zfill(4)
            if e == 1:
                morse += ' '
                morse += ':'

    morse = morse.replace('0', '.')
    morse = morse.replace('1', '-')

    return morse
