def fibonacci(n, x=0, y=1):
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return fibonacci(n - 1, x=y, y=(x + y))

def sum_of_even_fibonacci_up_to(k):
    even_numbers = []
    i = 0
    while fibonacci(i) < k:
        if fibonacci(i) % 2 == 0:
            even_numbers.append(fibonacci(i))
        i += 1
    return sum(even_numbers)
