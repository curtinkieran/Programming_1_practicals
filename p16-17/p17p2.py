'''define the function to find common divisors
    initialise tuple to (1, )
    enter for loop (2, find minimum number (half of this plus 1))
        if both numbers are divisible by the iteration:
            divisors += iteration
    add input of function to tuple.

print the function and supply 2 arguments'''



def commondivisors(num1, num2):
    divisors = (1, )
    for i in range(2, (min(num1, num2)//2) +1):
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i,)
    divisors += (min(num1, num2), )
    return divisors

print(commondivisors(50, 100))