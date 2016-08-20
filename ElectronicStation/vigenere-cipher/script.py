import string
def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    au = string.ascii_uppercase
    # Make all alphabets starting each alphabet at each old_encrypted letter
    myalphabs = [au[au.index(old_encrypted[e]):] + au[:au.index(old_encrypted[e])] for e, x in enumerate(old_encrypted)]

    # crawl old dec until D, what's index? aka yield letter of cipher
    cipher = [e for l_dec, alphab in zip(old_decrypted, myalphabs) for e, l in enumerate(alphab) if l == l_dec]

    # real dirty check where/if cipher repeats
    cipher2 = list(cipher)
    m = False
    break2 = False
    one = cipher.pop(0)
    two = cipher.pop(0)
    for e, i in enumerate(cipher2):
        try:
            if i == one and cipher2[e+1] == two and e >1:
                cipher = cipher2[:e]
                m = True
                # Another check here for AAAAAAAAA test. should b able to take all of cipher and repeatedly match cipher two
                cipher *= 150
                _cipher, m = check_to_end(cipher, cipher2, m)
                if m:
                    break
                else:
                    break2 = True
                    cipher = list(_cipher)
                    break
        except IndexError:
            #we're at the end of list
            break
    if not m and not break2:
        cipher.insert(0, two)
        cipher.insert(0, one)

    # use cipher against new_enc: (enc_letter + cipher) mod 26
    mystr = [au[(au.index(l) + c) % 26] for l, c in zip(new_encrypted, cipher)]
    return ''.join(mystr)


def check_to_end(cipher, cipher2, m):
    for i, j in zip(cipher, cipher2):
        if i != j:
            cipher = list(cipher2)
            m = False
            # found break in pattern down the list
            return cipher, m
    m = True
    # pattern goes to end
    return cipher, m
