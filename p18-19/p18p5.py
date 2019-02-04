'''define function():
first of all check to see if the forst 3 characters are == xyz. (otherwise xyz. would return false by methodd below, because x[i-1] == .
     then enter for loop for range(0, length input -2):
        search for string of length 3 that == xyz and make sure it is not preceeded by ".":
            return true'''

def find(x):
    if x[0:3] == "xyz":
        return True
    else:
        for i in range(0, len(x)-2):
            return x[i:i+3] == "xyz" and x[i-1] != "."
        

str = input("Enter a string: ")
print(find(str))