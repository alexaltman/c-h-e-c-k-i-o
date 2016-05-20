def min(*args, **kwargs):
    key = kwargs.get("key", None)
    mymin = 'None'

    if len(args) > 1:
        for i in args:
            if mymin == 'None':
                mymin = i
            elif key:
                if key(i) < key(mymin):
                    mymin = i
            else:
                if i < mymin:
                    mymin = i
        return mymin
    else:
        for i in args:
            for x in i:
                if mymin == 'None':
                    mymin = x
                elif key:
                    if key(x) < key(mymin):
                        mymin = x
                else:
                    if x < mymin:
                        mymin = x
        return mymin


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    mymax = 'None'

    if len(args) > 1:
        for i in args:
            if mymax == 'None':
                mymax = i
            elif key:
                if key(i) > key(mymax):
                    mymax = i
            else:
                if i > mymax:
                    mymax = i
        return mymax
    else:
        for i in args:
            for x in i:
                if mymax == 'None':
                    mymax = x
                elif key:
                    if key(x) > key(mymax):
                        mymax = x
                else:
                    if x > mymax:
                        mymax = x
        return mymax


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"

