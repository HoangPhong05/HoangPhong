# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:08:04 2024

@author: Hoang Phong
"""

P=float(input("nhap bien so xe cua ban"))
a=P//10000
b=(P%10000)//1000
c=((P%100000)%1000)//100
d=(((P%10000)%1000)%100) //10
e=(((P%10000)%1000)%100)%10
Y=(a+b+c+d+e)%10
print("so nut xe cua ban la:",Y)
