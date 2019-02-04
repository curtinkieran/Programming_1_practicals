'''pseudocode
prompt for integer

count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0

while number >= 0:
    if number = 0:
        count1+=1
    elif 0 <= number <= 20: etc etc'''

number = int(input('Enter a number: '))

count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0

while number >= 0:
    if number == 0:
        print('Number is 0')
        count1 += 1
    if 0 < number <= 20:
        print('Number is < 0 and <=20')
        count2 += 1
    if 20 < number <= 40:
        print('Number is < 20 and <=40')
        count3 += 1
    if 40 < number <= 60:
        print('Number is < 40 and <=60')
        count4 += 1
    if 60 < number <= 80:
        print('Number is < 60 and <=80')
        count5 += 1
    if 80 < number <= 100:
        print('Number is < 80 and <=100')
        count6 += 1
    if number > 100:
        print('Number is greater than 100')
        count7 += 1
    number = int(input('Enter a number: '))


print('equal to zero', '', count1)
print('0-20', '', count2)
print('20-40', '', count3)
print('40-60', '', count4)
print('60-80', '', count5)
print('80-100', '', count6)
print('Greater than 100', '', count7)
    
        
    
