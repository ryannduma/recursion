def factorial(n):
    x = 1
    if n > 1:
        x = factorial(n-1)
    return n*x


print(factorial(6))
