num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))
found_odd = False
highest=0

if num1%2==0 and num2%2==0 and num3%2==0:
    print('All numbers are even')

if num1 %2 !=0:
    found_odd = True
    highest = num1

if num2 %2 !=0:
    if found_odd == True:
        if num2>highest:
            highest = num2
    else:
        found_odd = True
        highest = num2

if num3 %2 !=0:
    if found_odd == True:
        if num3>highest:
            highest = num3
    else:
        found_odd = True
        highest = num3

if highest !=0:
    print(highest, 'is the largest odd number')

            
    
    
