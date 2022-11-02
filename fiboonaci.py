# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 11:03:27 2022

@author: SANTANU
"""

def fibbo(n):
    if n<=1:
        return n
    
   
    
    return fibbo(n-1)+fibbo(n-2)
    




n=int(input())
res=fibbo(n)