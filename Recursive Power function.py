# intro

def power(a, b):
    return a ** b

def c(n):
    if n > 1:
       print(c(n-1))
    return n


#x = power(2, 64)#
# x = x + power(x-1, x)
print(x) # print(power(x, x))
print(c(5))
