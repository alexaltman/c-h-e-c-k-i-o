class checkio:

    def __init__(self, atruevalue):
        self.atruevalue = atruevalue

    @staticmethod
    def __cmp__(atruevalue):
        return True

    @staticmethod
    def __eq__(atruevalue):
        return True

    @staticmethod
    def __lt__(atruevalue):
        return True

    @staticmethod
    def __le__(atruevalue):
        return True

    @staticmethod
    def __ne__(atruevalue):
        return True

    @staticmethod
    def __ge__(atruevalue):
        return True

    @staticmethod
    def __gt__(atruevalue):
        return True

if __name__ == '__main__':
    import re
    import math

    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'

    print('NO WAY :(')
