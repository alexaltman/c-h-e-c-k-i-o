FIRST_TEN = { "1": "one",
              "2": "two",
              "3": "three",
              "4": "four",
              "5": "five",
              "6": "six",
              "7": "seven",
              "8": "eight",
              "9": "nine"}
SECOND_TEN = { "10": "ten",
               "11": "eleven",
               "12": "twelve",
               "13": "thirteen",
               "14": "fourteen",
               "15": "fifteen",
               "16": "sixteen",
               "17": "seventeen",
               "18": "eighteen",
               "19": "nineteen"}
OTHER_TENS = { "2": "twenty",
               "3": "thirty",
               "4": "forty",
               "5": "fifty",
               "6": "sixty",
               "7": "seventy",
               "8": "eighty",
               "9": "ninety"}
HUNDRED = "hundred"


def checkio(number):
    leftmost_digit = ""
    second_digit = ""
    third_digit = ""

    number = str(number).strip()
    count = 0
    for i in number:
        count += 1
        if not leftmost_digit:
            leftmost_digit = i
            continue
        if not second_digit:
            second_digit = i
            continue
        if not third_digit:
            third_digit = i
            break

    if count == 3:
        trei = three_digits(leftmost_digit, second_digit, third_digit)
        return trei
    if count == 2:
        duex = two_digits(leftmost_digit, second_digit)
        return duex
    if count == 1:
        un = FIRST_TEN[leftmost_digit]
        return un

def three_digits(leftmost_digit, second_digit, third_digit):
    add_to_str = "hundred"
    if second_digit == "1":
        leftmost_digit = FIRST_TEN[leftmost_digit]
        second_digit = SECOND_TEN[(second_digit + third_digit)]
        return leftmost_digit + " " + add_to_str + " " + second_digit
    elif second_digit == "0" and third_digit == "0":
        print(leftmost_digit)
        return FIRST_TEN[leftmost_digit] + " " + add_to_str
    else:
        leftmost_digit = FIRST_TEN[leftmost_digit]
        if second_digit == "0":
            second_digit = ""
            third_digit = FIRST_TEN[third_digit]
            return leftmost_digit+" " +add_to_str +" "+third_digit
        else:
            second_digit = OTHER_TENS[second_digit]
            if third_digit == "0":
                return leftmost_digit+" " +add_to_str +" "+\
                       second_digit
            third_digit = FIRST_TEN[third_digit]
            return leftmost_digit+" " +add_to_str +" "+\
                   second_digit+" "+third_digit

def two_digits(leftmost_digit, second_digit):
    if leftmost_digit == "1":
        leftmost_digit = SECOND_TEN[(leftmost_digit + second_digit)]
        return leftmost_digit
    elif second_digit == "0":
        return OTHER_TENS[leftmost_digit]
    else:
        leftmost_digit = OTHER_TENS[leftmost_digit]
    second_digit = FIRST_TEN[second_digit]
    return leftmost_digit + " " + second_digit
