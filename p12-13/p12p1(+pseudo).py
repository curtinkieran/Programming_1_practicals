'''define function for getting factorial
prompt user for input
check if greater than 0
call factorial function and print answer
if < 0 print error message'''

import time

def fact(x):
    answer=1
    for i in range(1, x+1):
        answer*=i
    return answer

number = int(input('Enter a number: '))

if number >= 0:
    t0=time.time()
    print('Factorial of ', number, 'is', fact(number))
    t1=time.time()
else:
    print('An appropriate error message')


total = t1-t0

print(total)
