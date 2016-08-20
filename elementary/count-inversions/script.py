def count_inversion(sequence):

    count = 0
    for e, i in enumerate(sequence):
        for x in sequence[(e + 1):]:
            if i > x:
                count += 1
    return count
