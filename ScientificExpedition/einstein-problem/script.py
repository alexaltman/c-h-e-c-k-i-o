COLORS = ['blue', 'green', 'red', 'white', 'yellow']
PETS = ['cat', 'bird', 'dog', 'fish', 'horse']
BEVERAGES = ['beer', 'coffee', 'milk', 'tea', 'water']
CIGARETTES = ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield', 'Marlboro']
NATIONALITY = ['Brit', 'Dane', 'German', 'Norwegian', 'Swede']
NUMBERS = ['1', '2', '3', '4', '5']
QUESTIONS = {"number": NUMBERS, "color": COLORS, "nationality": NATIONALITY, "beverage": BEVERAGES,
             "cigarettes": CIGARETTES, "pet": PETS}

from itertools import combinations, chain
def answer(re, qu):       # qu: fish-color, tea-number
    re = [set(x.split('-')) for x in re]

    newl = []
    tmp = set()
    for r in re:
        # union all items in re that union with r
        tmp = r.union(*[r2 for r2 in re if r2.intersection(r)])
        if tmp not in newl:
            if not newl:
                newl.append(tmp)
            else:
                # Find if tmp has intersection w/ an existing item and break
                for e, i in enumerate(newl):
                    if i.intersection(tmp):
                        newl[e] = i.union(tmp)
                        break
                else:
                    # There was no intersection w/ existing items AND item wasn't in newl
                    newl.append(tmp)

    # Separate out completed sets
    houses = [x for x in newl.copy() if len(x) == 6]
    [newl.remove(x) for x in houses]

    for x, y in combinations(newl.copy(), 2):
        tmp = {}
        if len(x) + len(y) <= 6:
            # if they don't share any categories then merge and append to house if not in house already
            switch = False
            for c in [COLORS, PETS, BEVERAGES, CIGARETTES, NATIONALITY, NUMBERS]:
                if x.intersection(c) and y.intersection(c):
                    switch = True
            if not switch:
                tmp = x.union(y)
                if tmp not in houses:
                    houses.append(tmp)
                    newl.remove(x)
                    newl.remove(y)

    # add remaining - no combination with existing possible
    [houses.append(i) for i in newl]


    # determine unused
    unused = []
    for i in chain(COLORS+PETS+BEVERAGES+CIGARETTES+NATIONALITY+NUMBERS):
        used = False
        for h in chain.from_iterable(houses):
            if i == h:
                used = True
                break
        if not used:
            unused.append(i)

    # Assign unused to incomplete houses
    for u in unused:
        for c in [COLORS, PETS, BEVERAGES, CIGARETTES, NATIONALITY, NUMBERS]:
            if u in c:
                for h in houses.copy():
                    if len(h) < 6:
                        if not h.intersection(c):
                            houses.remove(h)
                            h.add(u)
                            houses.append(h)
                            break

    # get answer to question
    hint, q = qu.split('-')
    for house in houses:
        if hint in house:
            return house.intersection(QUESTIONS[q]).pop()
