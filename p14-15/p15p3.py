'''define the function
prompt for input
enter while loop:
    enter for loop, limit = input:
        print statement that shows progression towards the base case and calls function
    prompt for input'''

def series(x):
    if x == 0:
        return 13
    elif x == 1:
        return 8
    else:
        return((series(x-2)) + ((13)*(series(x-1))))

number = int(input("Enter a number: "))

while number >= 0:
    for i in range(0, number):
        print("Term number", i, "in series of length", number, "is:", series(i))
    number = int(input("Enter a number: "))
