def flat_list(a):
    m=[]
    for x in a:
        if hasattr(x, '__iter__'):r=flat_list(x);m+=r
        else:m.append(x)
    return m
