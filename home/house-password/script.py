def checkio(data):
    import re

    # data can't be empty
    if not data:
        return False

    # search for a number in string
    regex = r'[0-9]'
    matches = re.search(regex, data)
    #print(matches.group())
    if not matches:
        return False

    # Be more than 10 characters in length
    if len(data) < 10:
        return False

    # search for uppercase letter
    regex2 = r'[A-Z]'
    matches2 = re.search(regex2, data)
    if not matches2:
        return False

    # search for lowercase letter
    regex3 = r'[a-z]'
    matches3 = re.search(regex3, data)
    if matches3:
        num_matches3 = len(matches3.group())
        if num_matches3 == 0:
            return False
    else:
        return False
    print("five")
    return True



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

