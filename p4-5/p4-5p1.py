currency_amt_euro= float(input("Enter an amount: "))
conversion_to_pound = 0.89
product = currency_amt_euro*conversion_to_pound
if currency_amt_euro < 0:
    print ("Amount must be >=0. Please try again")
else:
    print (product)
                    
