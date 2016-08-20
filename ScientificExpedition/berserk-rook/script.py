def berserk_rook(berserker, enemies):
    berserker = set(berserker)
    enemies = [set(i) for i in enemies]

    def isclear(curr, i, myenemies):
        start = (curr - i).pop()
        end = (i - curr).pop()

        for e in myenemies:
            if e.intersection(curr) and e.intersection(i) and e != curr and e != i:
                isbw = (e - curr).pop()

                if end > start:
                    if start < isbw < end:
                        return False
                elif start > end:
                    if end > isbw > start:
                        return False
        return True

    def findnxt(curr, seen, cnt):
        myenemies = [e for e in enemies if e not in seen]
        for i in myenemies:
            if curr.intersection(i) and i not in seen and isclear(curr, i, myenemies):
                cnt = max(cnt, findnxt(i, seen+[i], len(seen)+1))
        return cnt

    tot = 0
    for i in enemies:
        if berserker.intersection(i) and isclear(berserker, i, enemies):
            tot = max(tot, findnxt(i, [i], 1))
    return tot
