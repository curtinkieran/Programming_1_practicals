'''define a function to get max of 2 input
prompt for 1 number
prompt for another number
print ( ... max (number1, number2))'''

def max(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))

print('The largest of', num1, 'and', num2, 'is', max(num1, num2))

print('Finshed!')