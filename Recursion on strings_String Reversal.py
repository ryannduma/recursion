# implement a program to reverse a string

# iterative method
"""
def elreverso(s):
    a = str(s)
    for i in range(1, len(a) + 1):
        b = len(a)
        c = (a[b - i])
        print(c)

    return c

elreverso("Here's a recursion reversal")
"""
# recursive

def lareverso(s): # ask sir for the other methods to do this
    n = len(s)

    if n == 0:
        return s
    else:
        c = lareverso(s[1:]) + s[0]
        return c


print("The reversed string is: ", end="")
print(lareverso("Here's a recursion reversal"))
