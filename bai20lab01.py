# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:19:12 2024

@author: Hoang Phong
"""

a=int(input("nhap a"))
b=int(input("nhap b"))
c=int(input("nhap c"))
ab= a if a>b else b
abc=ab if ab>c else c
print("so lon nhat la",abc)