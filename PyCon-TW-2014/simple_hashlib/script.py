import hashlib

def checkio(hashed_string, algorithm):
    return eval('hashlib.' + algorithm)(bytes(hashed_string, 'utf-8')).hexdigest()
