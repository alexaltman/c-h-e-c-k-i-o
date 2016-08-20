def checkio(ns):
    ns = [0] + ns + [0]

    def nxtstair(e, ns):

        if e == len(ns)-1:
            return 0
        if ns[e+1] > 0 and ns[e+2] > 0:
            print(ns[e+1])
            return ns[e+1] + nxtstair(e+1, ns)

        # Lookahead if possible to make decision
        if e+4 <= len(ns) - 1:
            fir = ns[e+1] + max([ns[e+2], ns[e+3]])
            sec = ns[e+2] + max([ns[e+3], ns[e+4]])
        elif e+3 <= len(ns) - 1:
            fir = ns[e+1] + max([ns[e+2], ns[e+3]])
            sec = ns[e+2] + ns[e+3]
        elif e+2 <= len(ns) - 1:
            fir = ns[e+1] + ns[e+2]
            sec = ns[e+2]
        elif e+1 <= len(ns) -1:
            fir = ns[e+1]
            sec = ''

        if not sec and sec != 0:
            print(ns[e+1])
            return ns[e+1] + nxtstair(e+1, ns)
        elif fir == sec: # if eq then sec since one will be neg. otherwise caught in 3rd if
            return ns[e+2] + nxtstair(e+2, ns)
        elif max([fir, sec]) == fir:
            print(ns[e+1])
            return ns[e+1] + nxtstair(e+1, ns)
        else:
            print(ns[e+2])
            return ns[e+2] + nxtstair(e+2, ns)

    return nxtstair(0, ns)
