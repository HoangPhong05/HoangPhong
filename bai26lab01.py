# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:04:41 2024

@author: Hoang Phong
"""
1.
a=int(input("nhap a"))
b=int(input("nhap b"))
c=int(input("nhap c"))
if a>b:
    a,b=b,a
if b>c:
    b,c=c,b
if a>c:
    a,c=c,a
else:
    print("khong xac dinh")
print("thu tu tang dan la :",a,b,c)

2.
N=int(input("nhap vao so nguyen N"))
x=N//100
y=(N//10)%10
z=N%10
if x>y:
    x,y=y,x
if y>z:
    y,z=z,y
if x>z:
    x,z=z,x
else:
    print("khong xac dinh")
P=x*100+y*10+z
print("con so co thu tu tang dan la:",P)    
    