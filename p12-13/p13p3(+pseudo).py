'''define a function with zero arguments
prompt for input within the function
print (within the function again)
return zero
call function'''

def print_max():
    def max(a,b):
        if a > b:
            return a
        else:
            return b

    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a number: '))

    print('The largest of', num1, 'and', num2, 'is', max(num1, num2))
    
    return

print(print_max())



