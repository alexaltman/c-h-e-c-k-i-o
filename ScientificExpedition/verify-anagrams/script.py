def verify_anagrams(first_word, second_word):
    first_word = list(first_word.replace(" ", "").lower())
    second_word = list(second_word.replace(" ", "").lower())

    if not len(first_word) == len(second_word):
        return False
    else:
        for i in first_word:
            try:
                second_word.remove(i)
            except ValueError as e:
                return False
        return True
