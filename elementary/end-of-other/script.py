def checkio(words_set):
    import re

    match = ""
    for word in words_set:
        regex = re.compile(r'{0}$'.format(word))
        for word2 in words_set:
            if word == word2:
                continue
            else:
                match = re.search(regex, word2)
                if match is not None:
                    return True


    return False
