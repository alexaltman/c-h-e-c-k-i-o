def checkio(expression):

    brkts =  {']': '[',
              '}': '{',
              ')': '(',
              }
    r_brkts = brkts.keys()
    l_brkts = brkts.values()

    order_brkts = []
    for i in expression:
        if i in brkts.keys() or i in brkts.values():
            order_brkts.append(i)

    if not order_brkts:
        return True
    elif order_brkts[0] not in brkts.values():
        return False

    last_opened = []
    for e, i in enumerate(order_brkts):
        if i in brkts.values():
            last_opened.append(i)
        elif i in brkts.keys():
            partner = brkts[i]
            if not last_opened:
                return False
            elif partner != last_opened[-1]:
                return False
            else:
                last_opened.pop()
    if last_opened:
        return False
    return True
