# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:30:57 2024

@author: Hoang Phong
"""

A=int(input("v:hinh vuong,n :hinh chu nhat,t:hinh tron "))
if A==v:
    canh=int(input("nhap do dai canh hinh vuong"))
    P= canh*4
    S=canh**2
    print("chu vi hinh vuong =",P,"dien tich hinh vuong =",S)
elif A==n:
    chieu rong=int(input("nhap chieu rong hinh chu nhat"))
    chieu dai = int(input("nhap chieu dai hinh chu nhat"))
    P=(chieu rong + chieu dai)*2
    S=chieu dai * chieu rong
    print("chu vi hinh chu nhat= ",P,"dien tich hinh chu nhat=",S)
elif A==t:
    ban kinh =int(input("nhap ban kinh hinh tron"))
    P=  ban kinh*2*3.14
    S= ban kinh **2*3.14
    print("chu vi hinh tron=",P,"dien tich hinh tron =",S)
else:
    print("khong xac dinh")    