password = 'python'
attempt = str(input('Enter a password: '))

#This exercise is ambiguous.  Do you want the user to input their
#password 3 times under one prompt?
#Or be prompted 3 separate times for their password?

count=0

if attempt == password:
    print('You have successfully logged in')
   
if attempt != password:
    print('Sorry, the password is wrong')
    print('You will have to enter your password 3 times')
    while count<3:
        attempt2 = str(input('Enter a password: '))
        if attempt2 == password:
            count+=1
        elif attempt2 != password:
            print('You have been denied access')
            break
    if count == 3:
        print('You have successfully logged in')

    
                
