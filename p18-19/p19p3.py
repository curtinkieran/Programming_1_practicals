'''define the function
    import os
    check if file exists, if so open it.
    initialise counts to 0
    for line in file:
        for character in line:
            if character = one of the bracket symbols:
                incriment count
            **do this for all 8**
    print all 8 totals.
    if sum (evencounts) == sum (oddcounts):
        print (message)
'''
def checkbracket(x):
    import os
    if os.path.isfile(x):
        print("Opening file 'Brackets' for reading")
        file = open(x, "r")
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    for l in file:
        for c in l:
            if c == "(":
                c1 += 1
            if c == ")":
                c2 += 1
            if c == "<":
                c3 += 1
            if c == ">":
                c4 += 1
            if c =="{":
                c5 +=1
            if c == "}":
                c6 +=1
            if c == "[":
                c7 += 1
            if c == "]":
                c8 += 1
    print("Total number of '(' =", c1)
    print("Total number of ')' =", c2)
    print("Total number of '<' =", c3)
    print("Total number of '>' =", c4)
    print("Total number of '{' =", c5)
    print("Total number of '}' =", c6)
    print("Total number of '[' =", c7)
    print("Total number of ']' =", c8)
    if (c1 + c3 + c5 + c7) == (c2 + c4 + c6 + c8):
        print("The file has balanced brackets")
    file.close()

checkbracket("brackets.txt")

    