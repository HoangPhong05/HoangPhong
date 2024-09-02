# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:53:29 2024

@author: Hoang Phong
"""



a=int(input("nhap a"))
b=int(input("nhap b"))
c=int(input("nhap c"))
d=int(input("nhap d"))
ab  = a if a<b else b
abc = ab  if ab < c else c
abcd  = abc if abc  <d else d
print(" so co gia tri nho nhat la",abcd )


    
    