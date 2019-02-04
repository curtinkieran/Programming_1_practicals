'''pseudocode
prompt +ve int

sum =0
count = 0
if int > 0:
    
    while x > count:
        sum += int
        count += 1
    print sum
    prompt +ve int pseudocode was wrong so I had to change it later on'''

total = 0
count = 0

number = int(input('Enter a positive number: '))

if number > 0:
    while number >= count:
        total += count
        count+=1
        if count > number:
            print(total)
            print()
            number = int(input('Enter a positive number: '))
            count = 0
            total = 0
      
    
    
