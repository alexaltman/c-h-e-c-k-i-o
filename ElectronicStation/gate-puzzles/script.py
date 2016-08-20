def find_word(message):
    message = message.lower()
    tots =[]
    words = message.replace('.', '').replace(',','').split(" ")

    for e, tstword in enumerate(words):
        avg_l = []
        for e2, word in enumerate(words):
            tmp = 0
            if e2 == e:
                continue

            if tstword[0] == word[0]:
                tmp += .10

            if tstword[-1] == word[-1]:
                tmp += .10

            if len(tstword) <= len(word):
                tmp += (len(tstword) / len(word)) * .30
            else:
                tmp += (len(word) / len(tstword)) * .30
            #get uniques
            unqs = set(word+tstword)
            tmp += (len(set(tstword).intersection(word))  / len(unqs)) * .50
            avg_l.append(tmp)

        #compute avg for tstword
        myavg = sum(avg_l) / len(avg_l)
        tots.append([tstword, myavg])

    #sort on list of list's second element
    tots.sort(key=lambda x: x[1])
    return tots[-1][0]
