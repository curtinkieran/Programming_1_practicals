'''define function to find common divisors found in lecture notes.
print function, supply 2 arguments'''

def commondivisors(num1, num2):
    divisors = ()
    for i in range(1, min(num1, num2) +1):
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i,)
    return divisors

print(commondivisors(36, 12))
