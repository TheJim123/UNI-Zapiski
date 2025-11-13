def sum_of_multiples(o, p, n):
    ''' Summs the multiples of "o" and "p", up to "n" '''
    multiples =[]
    for number in range(1, n):
        if number % o == 0:
            multiples.append(number)
        elif number % p == 0:
            multiples.append(number)
    return sum(multiples)
