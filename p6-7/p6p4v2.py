password = 'Programming'
count=0

while count < 3:
    attempt= str(input('Enter your password: '))
    if attempt != password:
        count+=1
        if count < 3:
            print ("Try again")
    else:
        print ('You have been successfully logged in')
        break
if count == 3:
    print('You have been denied access')

    

        
