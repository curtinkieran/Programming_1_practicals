'''define function to find string segment
    initialise count to 0 for cat and dog
    convert all letters to lower case
    for loop for (0, length of string(x))
        slice the string in segment of 3, if this == cat:
            incriment catcount
    do the same for loop for dog (0, len(string))
        if == dog:
            inceiment dogcount
    if catcount == dogcount:
        print(message)
    '''

def catdog(x):
    catcount = 0
    dogcount = 0
    x = x.lower()
    for a in range (0, len(x)):
        if x[a: a+3] == "cat":
            catcount += 1
    for b in range (0, len(x)):
        if x[b: b+3] == "dog":
            dogcount += 1
    if catcount == dogcount:
        print("cat and dog appear the same number of times in the string you entered.")

catdog("catcatCatdogdoGdog")