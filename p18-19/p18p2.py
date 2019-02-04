'''define function
    initialise count
    use for loop to iterate through length of input (but only up until the 3rd last character, as "code" is 4 long, no need
    to checck the last 3
        if a 4 string slice == "code":
            incriment count
        return count'''



def code(x):
    count=0
    for i in range(0, len(x)-3):
        if x[i:i+4] == "code":
            count+=1
    return count

str = input("Enter a string: ")
print(code(str))

        