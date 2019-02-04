'''
here we are calculating (input) number of terms of fibonacci
prompt for limit
f_0=0
f_1=1
fib = 0
while number > 0:
    if limit == 1:
        print('Series is: ', f_0)
    if limit == 1:
        print('Series is: ', f_0, f_1, sep =', ')
    while limit >= 2:
        print('Series is f1, f2, serp ', ', end='')
        a = f_1
        b = f_2
        x = 2

        while x < limit:
            fib= a + b
            print(', ', fib, end='')

            a=b
            b=fib
            x+=1'''

limit = int(input('Enter a number: '))
f_0=0
f_1=1
fib=0
if limit > 0:
    if limit == 1:
        print('Series is: ', f_0)
    elif limit >= 2:
        print('Series is:', f_0, ',', f_1, sep=' ', end='')   
        a=f_0
        b=f_1
        x=2
        while x < limit:
            fib=a+b
            print(', ', fib, end='')
            a=b
            b=fib
            x+=1
else:
    print('Number has to be greater than 0')
