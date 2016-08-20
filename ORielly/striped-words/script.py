VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = text.upper()

    wrd_cnt = 0
    last = ""
    current = ""
    striped_w = ""
    count = 0
    for e, i in enumerate(text):
        if len(text) == 1:
            return 0
        print(i)
        last = current
        if striped_w == False:
            if i.isalpha():
                continue
            elif i.isdigit():
                continue
            else:
                count = 0
                print(e, i, "stri w blank")
                striped_w = ""
                last = ""
                current = ""
                continue

        if i.isalpha():
            count += 1
            if i in VOWELS:
                current = "v"
            else:
                current = "c"
            if current == last:
                striped_w = False
            else:
                striped_w = True
                if e == (len(text)-1):
                    wrd_cnt += 1
        elif i.isdigit():
            striped_w = False
            current = ""
            last = ""
        else:
            if striped_w == True:
                if count > 1:
                    wrd_cnt += 1
                count = 0
                striped_w = ""
                last = ""
                current = ""

    return wrd_cnt
