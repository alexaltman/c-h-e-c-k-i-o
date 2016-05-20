def checkio(array):
    evens = []
    for i, v in enumerate(array):
        if i == 0 or i % 2 == 0:
            evens.append(v)

    try:
        last_item = array[-1]
    except IndexError as e:
        last_item = 1

    return (sum(evens) * last_item)



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"

