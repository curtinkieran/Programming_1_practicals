'''define the function for finding factorial (recursive)
print each value for x as it descends
wind out what the currnet factorial is
print value for currrent factorial'''

import sys
sys.setrecursionlimit(100000)

def fact(x):
    if x == 0:
        return 1
    else:
        currentfact = (x*(fact(x-1)))
        return currentfact
        
import time  

number= int(input('Enter a non-negtive number: '))

if number >= 0:
    t0=time.time()
    print(fact(number))
    t1=time.time()
    print('Completed')
else:
    print('You entered a negative number.')



total = t1-t0

print(total)