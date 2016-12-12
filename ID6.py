def sum_square(val):
    t = [i*j for i in range(1, val) for j in range(i+1, val+1)]
    return 2 * sum(t)
