'''define the function
prompt for input
enter while loop:
    enter for loop from range 1 to number +1:
        print statemment that shows progression towards the base case and also calls the function
    prompt for input'''
def series(x):
    if x==1:
        return 2
    if x > 1:
        return((x)+(series(x-1)))

number  = int(input("Enter a number: "))
while number > 0:
    if number < 1:
        print("Number has to be greater than or equal to 1")
    else:
        for i in range(1, number+1):
            print("The term number", i, "in series of length", number, "is:", series(i))
    number  = int(input("Enter a number: "))
    
