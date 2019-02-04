'''
limit = prompt for number
f_0=0
f_1=1
fib = 0 
if limit > 0:
    if limit == 1:
        print (Series is f_0)
    if limit >= 2:
        print (Series is f_0, f_1, sep=' ', end=''
        a=f_0
        b=f_1
        for x in range(2, limit)
        fib=a+b
        print(',', fib, end='')
        a=b
        b=fib
    prompt again'''

limit = int(input('Enter a number: '))
f_0=0
f_1=1
while limit >= 0:
    if limit == 0:
        print('You entered 0', end='')
    if limit == 1:
        print('Series is:', f_0, end='')
    if limit >= 2:
        print('Series is:', f_0, f_1, sep=',', end='')
        a=f_0
        b=f_1
        for x in range(2, limit):
            fib=a+b
            print(',', fib, end='')
            a=b
            b=fib
    print()
    limit = int(input('Enter a number: '))
    
