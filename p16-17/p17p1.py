'''define a function to find the factors of a number
    initialise factors tuple to (1, )
    enter for loop to chec if number is divisble by iteration ( but only go up as +1 past halfway)
        factors+=iteration
    add input of the function to the tuple

print function'''

def findfactors(x):
    factors = (1, )
    for i in range(2, (x//2)+1):
        if x % i == 0:
            factors += (i,)
    factors += (x,)
    return factors

print(findfactors(100))