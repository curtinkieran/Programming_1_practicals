'''define the function
    initialise count
    for loop for range (0, length of string-3):
        for each 4 strng slice:
            check each character individually
                incriment count if all correct
    return count'''

def code(x):        
    count=0
    for i in range(0, len(x)-3):
        if x[i] == "c" and x[i+1] == "o" and x[i+3] == "e" and x[i+2] in "abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUV":
                count+=1
    return count

str = input("Enter a string: ")
print(code(str))
