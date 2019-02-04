'''pseudocode
prompt for +ve int
factorial=0

if int = 0 print 1
if int = 1 print 1

for x in range (1, int):
    factorial=x*int'''

number = int(input('Enter a number: '))

factorial = 1


for x in range(1, number +1):
    factorial *= x
print(factorial)
