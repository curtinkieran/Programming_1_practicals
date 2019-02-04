'''define the function for finding factorial (recursive)
print each value for x as it descends
wind out what the currnet factorial is
print value for currrent factorial'''

def fact(x):
    if x == 0:
        return 1
    else:
        print('x is now: ', x)
        currentfact = (x*(fact(x-1)))
        print('Current factorial is ', currentfact)
        return currentfact
        
import time  

number= int(input('Enter a non-negtive number: '))
t0=time.time()
if number >= 0:
    fact(number)
    print('Completo')
else:
    print('You entered a negative number.')

t1=time.time()

total = t1-t0

print(total)