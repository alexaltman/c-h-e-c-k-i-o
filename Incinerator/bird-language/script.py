import re
def translate(phrase):
    for v in "aeiouy":
        phrase = re.sub(v+v+v, v, phrase)
    phrase = re.sub(r"([bcdfghjklmnpqrstvwxz])[aeiouy]", r'\1', phrase)
    return phrase
