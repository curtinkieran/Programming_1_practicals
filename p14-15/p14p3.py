''' prompt for input
enter for loop:
    enter another for loop:
        check if number is not prime:
            print message (z*x) and BREAK
    else:
        print that number is prime'''

number = int(input('Enter a number: '))

for i in range(1, number +1):
    for j in range(2, i):
        if i%j == 0:
            print(i, " is ", (j), " * ", int(i/j))
            break
    else:
        print(i, "is a prime number")
