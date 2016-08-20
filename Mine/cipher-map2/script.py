def recall_password(cipher_grille, ciphered_password):
    mystr = ''

    mystr += find4(cipher_grille, ciphered_password)
    #rotate 90
    rotate1 = list(zip(*cipher_grille[::-1]))
    mystr += find4(rotate1, ciphered_password)
    #rotate 90
    rotate2 = list(zip(*rotate1[::-1]))
    mystr += find4(rotate2, ciphered_password)
    #rotate 90
    rotate3 = list(zip(*rotate2[::-1]))
    mystr += find4(rotate3, ciphered_password)
    return mystr

def find4(cipher_grille, ciphered_password):
    mystr = ''
    for e, y in enumerate(cipher_grille):
        for e2, x in enumerate(y):
            if x == 'X':
                mystr += ciphered_password[e][e2]
    return mystr
