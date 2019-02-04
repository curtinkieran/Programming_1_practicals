year = int(input('Enter a year: '))

print('Year entered is:', year)

if year %4 != 0:
    print(year, 'is a common year')
elif year %100 != 0:
        print(year, 'is a leap year')
elif year %400 != 0:
        print(year, 'is a common year')
else:
    print(year, 'is a leap year')
    
