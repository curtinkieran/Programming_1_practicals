
'''pseudocode
number =0
while number >=0 :
    prompt imput
    calculate factorial

if number < 0:
    print'''

number = 0
factorial =1
while number >= 0:
    number = int(input('Enter a number: '))
    for x in range(1, number +1):
        factorial *= x
    if number>0:
        print('Factorial is', factorial)
        factorial = 1
        
