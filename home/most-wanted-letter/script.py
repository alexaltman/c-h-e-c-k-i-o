def checkio(text):

    alphabet = create_dict(text)
    print(alphabet)

    highest = []
    q = 0
    for k, v in alphabet.items():
        if v > q:
            q = v
            highest = []
            highest.append(k)
        elif v == q:
            highest.append(k)

    highest.sort()
    print(highest[0])
    return highest[0]


def create_dict(text):
    alphabetic = {}
    for i in text:
        i = i.lower()
        if "":
            continue
        elif i.isalpha() and i not in alphabetic:
            alphabetic[i] = 1
        elif i.isalpha() and i in alphabetic:
            alphabetic[i] += 1

    return alphabetic

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

