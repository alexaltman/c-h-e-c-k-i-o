def greatest_common_divisor(*args):
    gcd_start = min(args)
    factors = [i for i in range(2, gcd_start+1) if gcd_start %i == 0]
    final_factors = []
    for i in factors:
        if all(j % i == 0 for j in args):
            final_factors.append(i)

    if final_factors:
        return max(final_factors)
    else:
        return 1
