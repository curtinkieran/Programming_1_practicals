'''
prompt for strings
vowels = a e i o u
vowel count:
a=0
e=0
i=0
o=0
u=0
while loop:
    for i in string:
        if i = a, increment counta
        if i = e, increment e etc etc.
    print amount of each.
    re prompt for input.
'''


string = input('Enter a string: ')
while len(string) > 0:
    counta=0
    counte=0
    counti=0
    counto=0
    countu=0
    for i in string:
        if i == 'a' or i == 'A':
            counta += 1
        if i == 'e' or i == 'E':
            counte += 1
        if i == 'i' or i == 'I':
            counti += 1
        if i == 'o' or i == 'O':
            counto += 1
        if i == 'u' or  i =='U':
            countu += 1
    print('Number A\'s= ',counta)
    print('Number E\'s= ',counte)
    print('Number I\'s= ',counti)
    print('Number O\'s= ',counto)
    print('Number U\'s= ',countu)
    string = input('Enter a string: ')
        
