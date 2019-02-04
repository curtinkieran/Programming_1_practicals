''' define function for fib sequence
prompt user for input
check if greater than 0
call function for (input)
else print error'''

def fib(x):
    f_0=0
    f_1=1
    if x == 0:
        print(f_0)
    if x >= 2:
        print(f_0, f_1, sep=' ', end='')
    count=2
    a=f_0
    b=f_1
    while count < x:
        fib= a+b
        print(' ', fib, end ='')
        a = b
        b = fib
        count+=1
        
number = int(input('Enter a number: '))

if number >=0:
    fib(number)
else:
    print('You have entered a negative number')