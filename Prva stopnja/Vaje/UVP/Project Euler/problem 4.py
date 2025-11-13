def largest_palindrome(m, n):
    palindromic_numbers = []
    for i in range(m, n+1):
        for j in range(m, n+1):
            k = i * j
            if str(k) == str(k)[::-1]:
                palindromic_numbers.append(k)
    return max(palindromic_numbers)
