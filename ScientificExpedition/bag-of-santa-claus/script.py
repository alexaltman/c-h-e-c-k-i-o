import math

best = 0.0

def choose_good_gift(current_gift, gifts_in_bag, gift_number):
    global best

    if gift_number == 1:
        best = 0

    if gift_number < (gifts_in_bag / math.e):
        best = max(best, current_gift)
        return False

    return current_gift >= best
