# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:06:05 2022

@author: SANTANU

"""

def merge_sort(a):
    if len(a)>1:
        l_a=a[:len(a)//2]
        r_a=a[len(a)//2:]
        merge_sort(l_a)
        merge_sort(r_a)
        
        i=0
        j=0
        k=0
        while i<len(l_a) and j<len(r_a):
            if l_a[i]<r_a[j]:
                a[k]=l_a[i]
                i+=1
                k+=1
            else:
                a[k]=r_a[j]
                i+=1
                k+=1
        while i<len(l_a):
            a[k]=l_a[i]
            i+=1
            k+=1
        while j<len(r_a):
            a[k]=r_a[j]
            j+=1
            k+=1
    
    
a=[1,2,4,2,4]
merge_sort(a)
print(a)