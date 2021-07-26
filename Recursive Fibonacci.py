def fibonacci(n):

    if n < 0:
        print("The first fibonacci number is 0")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:

        return fibonacci(n-1) + fibonacci(n-2)  # print the n-th fibonacci number


def printfibonacci(n):  # this allows us to form the series in stead of just typing the nth term
    if n > 0:
        printfibonacci(n-1)
        print(fibonacci(n))


printfibonacci(6) # example - should yield - 1, 1, 2, 3, 5, 8

