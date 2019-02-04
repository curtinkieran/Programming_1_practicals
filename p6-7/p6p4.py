password= 'Programming'

count=0
while count<3:
    attempt= str(input('Enter your password: '))
    if attempt == password:
        print('You have successfully logged in')
        break
    else:
        count += 1 
        if count==3:
            print('You have been denied access')
        else:
            print('Try again')
            
        

    

        
