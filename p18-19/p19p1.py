'''define function that takes 2 arguments
    make an empty list
    while loop x!= 0:
        add x % y to the end of the list
        assign x value of "quotient" **convert this to an integer first!**
    reverse the list
    return list
prompt for 2 numbers
for i in list:
    print(i) and do not enter a new line'''

def changebase(x, y):
    conversion = []
    while x != 0:
        conversion.append(x%y)
        x = int(x/y)
    conversion.reverse()
    return conversion
        
    
    
num = int(input("Enter a number in base 10: "))
base = int(input("Enter the base you want to convert to: "))

for i in changebase(num, base):
    print(i, end="")
    


