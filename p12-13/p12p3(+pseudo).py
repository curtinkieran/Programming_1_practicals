'''define function for getting approx square root
prompt for input and convert to float
check if greater than 0
call function with (input, self selected tolerance)
else print message'''

def sq(number, epsilon):
    root = 0.0
    step = epsilon**2
    while abs(number-root**2) >= epsilon and root <= number:
        root += step
    if abs(number-root**2) < epsilon:
        print('Approx. square root of ', number, 'is', root)
    else:
        print('Failed to find the square root of ',number)
    
number = float(input('Enter a floating point number: '))
if number >= 0:
    sq(number, .01)
else:
    ('An appropriate error message')