'''
factorial of negative number not possible?  So i presume program is to
finish if neg number is entered?

prompt user for input
if number >= 0:
    count = 1
    for x in (0, input):
        count *= x
        print('Factorial is: ' count)
if number < 0:'''

number = int(input('Enter a number: '))

if number >= 0:
    count=1
    for x in range(1, number+1):
        count *= x
    print('Factorial of', number, 'is', count)
if number < 0:
    print('Number is less than 0')
    
        
