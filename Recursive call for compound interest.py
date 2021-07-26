total = 0
def compoundinterest(principal, rate, years): # enter the priciple amount, interest rate and number of years into the fn
    global total
    if years == 0:
        total = principal * rate
    else:
        total = compoundinterest(principal*rate, rate, years - 1)

    return total


compoundinterest(100, 1.05, 3)
print(total)
