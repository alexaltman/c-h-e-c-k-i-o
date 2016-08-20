import itertools

def checkio(chips):
    all_successes = []
    highest_possible = sum([max(i) for i in chips])
    # Permutate the chips through all possible locations
    for x in itertools.permutations(list(range(0,6))):
        # x[0] could be any index from the permutation of the list 0 to 6
        sums = perm_chips([chips[x[0]], chips[x[1]], chips[x[2]], chips[x[3]], chips[x[4]], chips[x[5]]])
        if sums:
            all_successes.extend(sums)
            # Return sooner if max points is reached
            if any([h == highest_possible for h in sums]):
                return highest_possible
        sums.clear()
    return max(all_successes)


def perm_chips(chips):
    successes = []
    # Permutate every position of the numbers within the chips without moving the chip's location
    for a in itertools.permutations(chips[0]):
        for b in itertools.permutations(chips[1]):
            for c in itertools.permutations(chips[2]):
                for d in itertools.permutations(chips[3]):
                    for e in itertools.permutations(chips[4]):
                        for f in itertools.permutations(chips[5]):
                            my_new_li = ''
                            myl = [a, b, c, d, e, f]
                            try:
                                my_new_li = test_li_pattern(list(itertools.chain(*myl)))
                            except ValueError:
                                pass

                            if my_new_li:
                                successes.append(my_new_li)
    return [0, get_highest_sum(successes)]

def test_li_pattern(myl):
    if ([myl[i] for i in [2, 5, 8, 11, 14]] == [myl[i] for i in [3, 6, 9, 12, 15]]) and (myl[0] == myl[-1]):
        return myl
    else:
        raise ValueError('le sook')


def get_highest_sum(lili):
    mysum, highest = 0, 0
    for li in lili:
        mysum = 0
        # Get every chip's outer (middle) number
        mysum = sum([i for i in li[1::3]])
        if mysum > highest:
            highest = mysum
    return highest
