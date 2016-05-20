r_nums = { 1: 'I',
           2: 'II',
           3: 'III',
           4: 'IV',
           5: 'V',
           6: 'VI',
           7: 'VII',
           8: 'VIII',
           9: 'IX',
           10: 'X',
           40: 'XL',
           50: 'L',
           90: 'XC',
           100: 'C',
           400: 'CD',
           500: 'D',
           900: 'CM',
           1000: 'M'}

def checkio(num):
    my_nums = r_nums.keys()
    my_roman = ""
    while num > 0:
        h = set_h(num, my_nums)
        my_roman += r_nums[h]
        num -= h
    return my_roman

def set_h(num, my_nums):
    set_highest = 0
    for i in my_nums:
        if i <= num:
            if i > set_highest:
                set_highest = i
    return set_highest

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
