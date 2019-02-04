income = float(input("Enter an amount: "))
larger = income*.6
smaller = income*.4
tax = (larger*.23)+(smaller*.41)
if income<0:
    print ("Amount of income must be >=0")
else:
    print (income)
    print (larger)
    print (smaller)
    print (tax)
    print (income-tax)
