def check_pangram(text):
    import string
    string.ascii_lowercase

    for i in string.ascii_lowercase:
        if i in text.lower():
            continue
        else:
            return False
    return True
