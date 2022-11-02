# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 06:18:33 2022

@author: SANTANU
"""

try:    
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b;    
    print("a/b = %d"%c)    
except:    
    print("can't divide by zero")    
else:    
    print("Hi I am else block")  

try:    
    #this will throw an exception if the file doesn't exist.     
    fileptr = open("file.txt","r")    
except IOError:    
    print("File not found")    
else:    
    print("The file opened successfully")    
    fileptr.close()    

try:    
    age = int(input("Enter the age:"))    
    if(age<18):    
        raise ValueError   
    else:    
        print("the age is valid")    
except ValueError:    
    print("The age is not valid")    