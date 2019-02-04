'''
prompt for integer
square = 0
check if square of that number is <= number.
increment by 1
if square == 0:
    print()
else:
    print()'''

root = 0
number = int(input('Enter a number: '))
while number > 0:
    while root**2 < number:
        root += 1
    if root**2 == number:
        print(root, 'is a square root of', number)
    else:
        print('Number does not have a square root')
    number = int(input('Enter a number: '))

print('Number is negative')
