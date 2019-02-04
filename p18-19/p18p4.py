'''Define function(x, y)
    convert both to lower case letters
    find the length of both
    if x = the final len(x) slice of y:
        print()
    elif y = the final len(y) slice of x:
        print()'''

def same(x,y):
    x = x.lower()
    y = y.lower()
    a = len(x)
    b = len(y)
    if x == y[-a:]:
        print(x, "appears at the end of", y)
    elif y == x[-b:]:
        print(y, "appears at the end of", x)
    else:
        print("Nothing to see here, Finished!")
    
a = input("Enter a string: ")
b = input("Enter a string: ")
same(a, b)