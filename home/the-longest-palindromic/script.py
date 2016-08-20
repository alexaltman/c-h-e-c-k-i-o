def longest_palindromic(text):
    largest = text[0:1]

    for e, i in enumerate(text):
        for n in reversed(range(len(text))):
            subs = text[e:n+1]
            if len(subs) > len(largest):
                if len(subs) > len(largest):
                    if len(subs) % 2 == 0:
                        if subs[0:(len(subs)//2)] == subs[len(subs)//2:][::-1]:
                            largest = subs
                    else:
                        if subs[0:(len(subs)//2)] == subs[(len(subs)//2)+1:][::-1]:
                            largest = subs
    return largest
