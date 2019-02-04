'''define the function
    include print statements to show progression towards the base case
    
prompt user for input
enter while loop (input >= to 1):
    call function'''

def series (x):
    if x == 1:
        print("about to print number 2 from the base case")
        return 2
    else:
        result = (2)*(series(x-1))
        print("About to print number", result, "from function with argument", x)
        return((2)*(series(x-1)))

number = int(input("Enter a number: "))

while number >= 1:
    series(number)
    number = int(input("Enter a number: "))

        


