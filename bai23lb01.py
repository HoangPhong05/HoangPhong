# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:59:52 2024

@author: Hoang Phong
"""

import math
print("ax**2+bx+c=0")
a=float(input("nhap a"))
b=float(input("nhap b"))
c=float(input("nhap c"))
denta=float()
denta=b**2-4*a*c
if denta<0:
    print("phuong trinh vo nghiem")
elif denta==0:
    x=(-b/(2*a))
    print("x la nghiem kep x=",x)    
else:
    x1=(-(b)+math.sqrt(denta)/(2*a))
    x2=(-(b)-math.sqrt(denta)/(2*a))    
    print("phuong trinh co 2 nghiem phan biet")
    print("x1=",x1)
    print("x2=",x2)