def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result
