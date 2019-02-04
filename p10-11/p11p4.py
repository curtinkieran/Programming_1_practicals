'''
define function for factorial
define function for catalan numbers
prompt for number
if == 0:
    print(ans)
if ==1:
    print(ans)
if > 1:
    count =2
    print()
    while loop count < number:
        assign variables for (2n)!, (n+1)!, and (n)!
        print cat fn (count)
        incriment count'''


def fact(x):
    if x >= 0:
        count=1
        for i in range(1, x+1):
            count *= i
        return int(count)
def cat(x):
    cat = a/(b*c)
    return int(cat)

series = int(input('Enter a number: '))
if series == 0:
    print('Series is 1')
if series == 1:
    print('Series is 1, 1')
if series > 1:
    count = 2
    print('Series is 1, 1', end='')
    while count < series:
        a = fact(2*count)
        b = fact(count+1)
        c = fact(count)
        print(',', cat(count), end='')
        count+=1
    
