def predict_ghost(L):
    L = list(L)
    return exp_smoothing(list(L)) + trend(list(L))

alpha = .8
def exp_smoothing(L):
        return alpha * L.pop() + (1 - alpha) * (predict_ghost(L) if L else 1)

beta = 1
def trend(L):
    if len(L) == 1:
        return 0
    elif L:
        return beta * (L.pop() - L[-1]) + (1 - beta) * (trend(L) if L else 0)
