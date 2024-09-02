# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:08:44 2024

@author: Hoang Phong
"""

import math
print("ax+b=o")
a=float(input("nhap a"))
b=float(input("nhap b"))
if  a==0:
    if b==0:
        print("phuong trinh co vo so nghiem")
    else:
        print("phuong trinh vo nghiem")
else:
    x=-b/a
    print("phuong trinh co nghiem duy nhat",x)