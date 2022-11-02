
import math
import cmath
#if the equation is a**2x+bx+c=0
a=float(input("enter the vaue of a: "))
b=float(input("enter the vaue of b: "))
c=float(input("enter the vaue of c: "))
s=b**2-4*a*c

if s>=0:
    R1=(-b+math.sqrt(s))/2.0*c
    R2=(-b-math.sqrt(s))/2.0*c
    print("the roots are", R1, R2)
else:
    R1=(-b+cmath.sqrt(s))/2.0*c
    R2=(-b-cmath.sqrt(s))/2.0*c
    print("the roots are", R1, R2)