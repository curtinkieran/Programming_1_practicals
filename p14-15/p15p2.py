''' define the function
prompt for input
enter while loop:
    enter for loop where limit is nummber+1:
        print statement that shows progression towards base case + calls function
    prompt for input'''

def series(x):
    if x == 1:
        return 1
    else:
        return((series(x-1)) + (2**x-1))

number = int(input("Enter a number: "))
while number >= 1:
    for i in range(1, number+1):
        print("Term number", i, "in series of length", number, "is:", series(i))
    number = int(input("Enter a number: "))
