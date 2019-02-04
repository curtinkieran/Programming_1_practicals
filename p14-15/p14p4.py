'''prompt for input
enter for loop:
    initialise a variable "foundprime" to keep track of if a prime number has been found
    enter second for loop:
        check if number is not prime:
            if not prime, print product of 2 numbers that make that number
            set foundprime to =0
    else:
        check if foundprime =1:
            if so, print(message)'''

number = int(input('Enter a number: '))

for i in range(1, number +1):
    foundprime=1
    for j in range(2, i):
        if i%j == 0:
            print(i, " is ", (j), " * ", int(i/j))
            foundprime=0
    else:
        if foundprime == 1:
            print(i, "is a prime number")
            
    
            