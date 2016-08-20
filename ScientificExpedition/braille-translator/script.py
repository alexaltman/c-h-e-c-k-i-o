import string

def convert(code):
    bin_code = bin(code)[2:].zfill(6)[::-1]
    return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]


L_N = list(map(convert,
                           [1, 3, 9, 25, 17, 11, 27, 19, 10, 26,
                            5, 7, 13, 29, 21, 15, 31, 23, 14, 30,
                            37, 39, 62, 45, 61, 53, 47, 63, 55, 46, 26]))
CAPITAL_FORMAT = convert(32)
NUM_FMT = convert(60)
PUNCT = {",": convert(2), "-": convert(18), "?": convert(38),
               "!": convert(22), ".": convert(50), "_": convert(36)}
WHITESPACE = convert(0)

s = string.ascii_lowercase

def braille_page(text: str):

    symbols = []
    for i in text:
        if i == ' ':
            symbols.append(WHITESPACE)
        elif i in PUNCT.keys():
            symbols.append(PUNCT[i])
        elif i.isupper():
            symbols.append(CAPITAL_FORMAT)
            symbols.append(L_N[s.index(i.lower())])
        elif i.isdigit():
            symbols.append(NUM_FMT)
            symbols.append(L_N[int(i) - 1])
        else: # reg lower
            symbols.append(L_N[s.index(i)])

    count, lines = 0, 0
    tt = [[], [], []]
    for sym in symbols:
        if count + 1 <= 10:
            count += 1
        else:
            tt.append([0]*len(tt[0]))
            tt.extend([ [], [], [] ])
            count = 1 # 1 not 0 since we're looping over count one already
            lines += 4

        if count < 10:
            tt[lines].extend(sym[0] + [0])
            tt[lines+1].extend(sym[1] + [0])
            tt[lines+2].extend(sym[2] +[0])
        elif count == 10:
            tt[lines].extend(sym[0])
            tt[lines+1].extend(sym[1])
            tt[lines+2].extend(sym[2])

    # line sizing
    for e, i in enumerate(tt):
        if len(i) < len(tt[0]):
            tt[e] = i + ([0]*(len(tt[0]) - len(i)))

    # remove leftovers on single short row
    if lines == 0:
        del tt[lines][-1]
        del tt[lines+1][-1]
        del tt[lines+2][-1]

    return tt
