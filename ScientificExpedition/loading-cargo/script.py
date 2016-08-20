from itertools import combinations

def checkio(weights):
    lowest = ''
    if len(weights) == 1: return weights[0]
    for h in range(1, len(weights)):
        for i in combinations(weights, h):
            leftovers = weights.copy()
            [leftovers.remove(j) for j in i]
            lowest = abs(sum(leftovers) - sum(i)) if lowest == str() else min(abs(sum(leftovers) - sum(i)), lowest)
    return lowest
