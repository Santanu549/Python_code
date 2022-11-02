# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 09:31:24 2022

@author: SANTANU
"""
"""
a="aeiou"
b="hkasdjdobh"
st=[]
c=0
flag=0
for j in range(len(b)):
    for i in range(len(a)):
        if b[j]==a[i]:
            flag=1
            break
        else:
            flag=0
    if flag==0:
        c = c + 1
    else:
        st.append(c)
        c=0
st.append(c)
d=max(st)
"""

t=int(input())
for i in range(t):
    n=int(input())
    b=str(input())[:n]
    a="aeiou"
    st=[]
    c=0
    flag=0
    for j in range(len(b)):
        for i in range(len(a)):
            if b[j]==a[i]:
                flag=1
                break
            else:
                flag=0
        if flag==0:
            c = c + 1
        else:
            st.append(c)
            c=0
    st.append(c)
    d=max(st)
    if d>=4:
        print('no')
    else:
        print('yes')
    