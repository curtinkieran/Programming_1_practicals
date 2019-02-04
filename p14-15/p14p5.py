'''define function
prompt for input
check if negative
enter for loop range 0 to input:
    print message that shows progression towards the base case and also calls the function'''

def fibrecur(x):
    if x <= 1:
        return x
    else:
        return(fibrecur(x-2)+fibrecur(x-1))

series = int(input("Enter the number of terms for the series: "))

if series < 0:
    print("Number entered needs to be greater than 0")
else:
    for i in range(series):
        print("Term number", i+1, "of", series, "is:", fibrecur(i))
        