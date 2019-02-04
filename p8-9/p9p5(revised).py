'''pseudocode
prompt for total_toppings (n)
prompt for standard amount (k)

total combinations=        n!
                       ---------
                        k!(n-k)!
'''

k=0
n=0

total_toppings = int(input('Enter a number: '))
factorial=1
for x in range(1, total_toppings +1):
    factorial *= x
n = factorial

standard_amount = int(input('Enter a number: '))
factorial=1
for x in range(1, standard_amount+1):
    factorial *= x
k = factorial

print('n!: ', n)
print('k!: ', k)
c= total_toppings - standard_amount
print('n-k: ', c)

factorial = 1
for x in range(1, c+1):
    factorial *= x
d=factorial
print('factorial n-k: ', d)

    
    

print(n/(k*d))
