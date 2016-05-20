import string

def safe_pawns(pawns):
    count = 0

    for i in pawns:
        set_back_left = back_left(i)
        print(set_back_left)
        set_back_right = back_right(i)
        print(set_back_right)

        if set_back_left in pawns or set_back_right in pawns:
            print(count)
            count += 1
    return count

def back_left(coord):
    for i in coord:
        for l in i:
            if l.isalpha():
                letter_index = string.ascii_lowercase.index(l)
                new_letter = string.ascii_lowercase[(letter_index - 1)]
            elif l.isdigit():
                new_digit = int(l) - 1
    return new_letter + str(new_digit)

def back_right(coord):
    for i in coord:
        for l in i:
            if l.isalpha():
                letter_index = string.ascii_lowercase.index(l)
                new_letter = string.ascii_lowercase[(letter_index + 1)]
            elif l.isdigit():
                new_digit = int(l) - 1
    return new_letter + str(new_digit)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

