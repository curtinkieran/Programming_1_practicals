'''this was taken from the lecture notes
define function 1:
    define function to convert to lower case and make sure input is all letters of the alphabet
        return the original string
    define function to check if palindrome:
        if length string <= 1:
            return True
        else return if first character is equal to last character, and call the function again only to check the remainder of the string

prompt for input
check if not an eempty string
enter while loop
    if function = True:
        print(message)
    else:
        print(message)
'''
def checkpal(x):
    def lower(x):
        x = x.lower()
        letstring=""
        for char in x:
            if char in "abcdefghijklmnopqrstuvwxyz":
                letstring += char
        return letstring
    def palind(x):
        if len(x) <= 1:
            return True
        else:
            return x[0] == x[-1] and palind(x[1:-1])
    return palind(lower(x))
    
str = input("Enter a string (emply string to exit): ")

while str != "":
    if checkpal(str):
        print(str, "is a palindrome")
    else:
        print(str, "is not a palindrome")
    str = input("Enter a string (empty string to exit): ")
print("Finished!")
