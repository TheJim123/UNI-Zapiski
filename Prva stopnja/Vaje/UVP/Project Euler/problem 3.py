def largest_prime_factor(k):
    ''' A pretty neat way of finding the largest prime factor'''
    p_factors = []
    i = 2
    while i * i < k:
        if k % i != 0:
            i += 1
        else:
            k //= i
            p_factors.append(i)
    if k > 1:
        p_factors.append(k)
    return max(p_factors)
