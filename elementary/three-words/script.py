def checkio(words):

    count = 0
    mylist = words.split(' ')
    for i in mylist:
        if i.isdigit():
            count = 0
            continue
        else:
            count +=1
            if count >= 3:
                return True
    return False
