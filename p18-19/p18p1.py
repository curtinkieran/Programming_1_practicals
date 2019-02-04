''' define function to convert to lower case
define function for checkinf if palindrome:
    while length of x > 1:
        check if first letter  == last letter:
            remove first and last letters from string and return true
            else return false
    if x == 1:
        return true
    else:
        return false'''
    
def lc(x):
    letstring = ""
    x = x.lower()
    for char in x:
        if char in "abcdefghijklmnopqrstuvwxyz":
            letstring+=char
    return letstring

def pal(x):
    while len(x) > 1:
        if x[0] == x[-1]:
            x = (x[1:-1])
            return True
        else:
            return False
    if len(x) == 1:
        return True
    else:
        return False
    


st = input("Enter a string: ")
print("All lower case is: ", lc(st))
st = lc(st)

if pal(st):
    print(st, "is a palindrome")
else:
    print(st, "is not a palindrome")







    