'''scoping refers to the places that you can see or have access to certain variables.
define a function
return q
assign values to variables
print what they are
call the function, assign value of variable to what the function returns
print what the variables are now that function has been called'''

def f(q):
    print('In function q: ')
    q+=1
    w=2
    print('q is: ', q)
    print('w is: ', w)
    print('e is: ', e)
    return q

q, w, e = 18, 19, 20
print('Before calling function')
print('q is: ', q)
print('w is: ', w)
print('e is: ', e)

e= f(w)

print('After funcation (q)')
print('q is: ', q)
print('w is: ', w)
print('e is: ', e)
