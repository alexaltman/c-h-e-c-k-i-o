def check_connection(network, first, second):

    count = 0
    if (first + "-" + second) in network or (second + "-" + first) in network:
        return True
    else:
        next_level = islinkedto(network, first)
        graveyard = []
        for i in next_level:
            graveyard.append(i)
            print("nextl")
            print(next_level)
            if (i + "-" + second) in network or (second + "-" + i) in network:
                return True
            else:
                lvl2 = islinkedto(network, i)
                if lvl2 is None:
                    return False
                for i2 in lvl2:
                    if i2 in graveyard:
                        continue
                    else:
                        next_level.append(i2)
        return False


def islinkedto(network, first):
    next_level = []
    for i in network:
        if first in i:
            x, y = i.split("-")
            if first != x:
                next_level.append(x)
            elif first != y:
                next_level.append(y)
    return next_level

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."

