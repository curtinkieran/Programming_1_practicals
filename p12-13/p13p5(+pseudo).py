'''scoping refers to the places that you can see or have access to certain variables.'''

def f(q):
    print('In function q: ')
    q+=1
    w=2
    r=200
    print('q is: ', q)
    print('w is: ', w)
    print('e is: ', e)
    print('r is: ', r)
    return r

q, w, e, r = 18, 19, 20, 100
print('Before calling function')
print('q is: ', q)
print('w is: ', w)
print('e is: ', e)
print('r is: ', r)

e= f(q)

print('After funcation (q)')
print('q is: ', q)
print('w is: ', w)
print('e is: ', e)
print('r is: ', r)
