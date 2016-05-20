def checkio(game_result):

    #check horizontal rows for win
    for row in game_result:
        xo = check_list_for_win(row)
        if xo == 1:
            continue
        elif xo == "O" or xo == "X":
            return xo


    #check vertical columns for win
    new_list = []
    new_list.append(game_result[0][0])
    new_list.append(game_result[1][0])
    new_list.append(game_result[2][0])
    xo = check_list_for_win(new_list)
    if xo == "O" or xo == "X":
        return xo

    new_list = []
    new_list.append(game_result[0][1])
    new_list.append(game_result[1][1])
    new_list.append(game_result[2][1])
    xo = check_list_for_win(new_list)
    if xo == "O" or xo == "X":
        return xo

    new_list = []
    new_list.append(game_result[0][2])
    new_list.append(game_result[1][2])
    new_list.append(game_result[2][2])
    xo = check_list_for_win(new_list)
    if xo == "O" or xo == "X":
        return xo


    #check diagnal for win (2 ways)
    diag_l_to_r = []
    diag_l_to_r.append(game_result[0][0])
    diag_l_to_r.append(game_result[1][1])
    diag_l_to_r.append(game_result[2][2])
    xo = check_list_for_win(diag_l_to_r)
    if xo == "O" or xo == "X":
        return xo

    #check diagnal for win (2 ways)
    diag_r_to_l = []
    diag_r_to_l.append(game_result[0][2])
    diag_r_to_l.append(game_result[1][1])
    diag_r_to_l.append(game_result[2][0])
    xo = check_list_for_win(diag_r_to_l)
    if xo == "O" or xo == "X":
        return xo

    return "D"

def check_list_for_win(listpls):
    count_x = 0
    count_o = 0
    for letter in listpls:
            if letter == ".":
                break
            elif letter == "X":
                count_x += 1
            elif letter == "O":
                count_o += 1

    if count_x == 3:
        return "X"
    elif count_o == 3:
        return "O"
    else:
        return 1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"


