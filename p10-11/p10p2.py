'''
prompt for number
intialise cube =0
while loop (number !=0):
    check cube <= number (absolute)
        increment
    if **3 == num, print
        *if input is negative, then change cube to -cube*
    else: print
    re prompt for number'''



number = int(input('Enter a number: '))
cube=0
while number != 0:
    while cube**3 < abs(number):
        cube += 1
    if cube**3 == abs(number):
        if number < 0:
            cube = -cube
        print(cube, 'is a cubed root of', number)
    else:
        print(number, 'does not have a cubed root')
    number = int(input('Enter a number: '))

