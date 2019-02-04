length= float(input("Enter a number: "))
import math
square= length**2
cube= length**3
circle= (math.pi)*(length**2)
sphere = (4/3)*(math.pi)*(length**3)
cylinder = (math.pi)*(length**2)*(length)
if length < 0:
    print ("Length must be >=0.  Please try again")
else:
    print (square)
    print (cube)
    print (sphere)
    print (cylinder)
