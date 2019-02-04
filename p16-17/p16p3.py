'''define the function
    initialise answer and factors to 0
    enter for loop (1 to input):
        if number modulus iteration of loop:
            factors += that iteration
        for loop to iterate through tuple of factors and add them together
            return true if this result == input

prompt for input
enter for loop:
    supply iteration of for loop as a argument for the function, if it is true:
        print(iteration)'''
def checkyperfectonumero(x):
    answer = 0
    factors = ()
    for i in range(1, x):
        if x % i == 0:
            factors += (i,)
    for b in factors:
        answer += b
    return x == answer
    
number = int(input("Please enter a number: "))
for i in range(1, number+1):
    if checkyperfectonumero(i):
        print(i)