'''define function
iterate through the input string, and convert all digits/letters to integers (create a list)
initialise number to 0 and count to len(x)-1
check that the number entered is compatible with the base entered
itierate through the list, and convert each number to base 10, and add them all together.'''
def convten(x, y):
    list = []
    for i in x:
        if i == "0":
            i = 0
            list.append(i)
        if i == "1":
            i = 1
            list.append(i)
        if i == "2":
            i = 2
            list.append(i)
        if i == "3":
            i = 3
            list.append(i)
        if i == "4":
            i = 4
            list.append(i)
        if i == "5":
            i = 5
            list.append(i)
        if i == "6":
            i = 6
            list.append(i)
        if i == "7":
            i = 7
            list.append(i)
        if i == "8":
            i = 8
            list.append(i)
        if i == "9":
            i = 9
            list.append(i)
        if i == "A" or i == "a":
            i = 10
            list.append(i)
        if i == "B" or i == "b":
            i = 11
            list.append(i)
        if i == "C" or i == "c":
            i = 12
            list.append(i)
        if i == "D" or i == "d":
            i = 13
            list.append(i)
        if i == "E" or i == "e":
            i = 14
            list.append(i)
        if i == "F" or i == "f":
            i = 15
            list.append(i)
    print("String converted to numbers in a list is: ", list)
    num = 0
    count = len(x)-1
    for i in list:
        if i >= y:
            print("You silly goose!", x, "is not a number in base", y, ".")
            result = False
            break
        else:
            num += (i)*(y**count)
            count -= 1
            result = True
    if result == True:
        print("Number when converted to base 10 is", num)
            
    return
            
num = input("Enter a number (in base 2-16): ")
base = int(input("And tell me, what base is this in?"))

convten(num, base)