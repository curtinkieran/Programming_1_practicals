'''import os.path
check if webpage is a file
check if results is a file
prompt for confirmation if it already exists
open files for reading and writing

initialise all counts to 0
for line in file:
    for char in file:
        check for characters:
            if so, incriment counter
    for character in range (0, length of line +1)
        cutinto appropriate slices and check if the relevant strings match

write each answer to the output file.  Convert to string first and add newline after'''

import os.path

if os.path.isfile("webpage.html"):
    fileHandle = open("webpage.html", "r")
if os.path.isfile("results.txt"):
    print("'results.txt' is already a file. Enter yes to open for writing.")
    answer = input("Enter yes or no: ")
    if answer == "yes":
        fileWrite = open("results.txt", "w")

countmorethan = 0
countlessthan = 0
lowercasee = 0
newlines = 0
endcom = 0
startcom = 0

for l in fileHandle:
    for c in l:
        if c == ">":
            countmorethan += 1
        if c == "<":
            countlessthan += 1
        if c == "e":
            lowercasee += 1
    for i in range(0, len(l)+1): 
        if l[i:i+2] == "\n":
            newlines += 1
        if l[i:i+3] == "-->":
            endcom += 1
        if l[i:i+4] == "<!--":
            startcom += 1
            
print("number of > in file is: ", countmorethan)
print("number of < in file is: ", countlessthan)
print("number of character 'e' in file is: ", lowercasee)
print("number of newlines in file is: ", newlines)
print("number of '-->' in file is: ", endcom)
print("number of '<!--' in file is: ", startcom)

fileWrite.write(str(countmorethan) + '\n')
fileWrite.write(str(countlessthan) + '\n')
fileWrite.write(str(lowercasee) + '\n')
fileWrite.write(str(newlines) + '\n')
fileWrite.write(str(endcom) + '\n')
fileWrite.write(str(startcom) + '\n')


fileHandle.close()
fileWrite.close()



            

