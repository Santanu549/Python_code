# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math #importing math to use sqrt() fuunction
a=float(input("enter the value of first side size: "))
b=float(input("enter the value of second side size: "))
c=float(input("enter the value of third side size: "))
s=(a+b+c)/2.0
d=(s*(s-a)*(s-b)*(s-c))
area=math.sqrt(d)
print("the area of the triangle is ",area)