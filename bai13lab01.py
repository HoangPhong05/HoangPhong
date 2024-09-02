# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:32:42 2024

@author: Hoang Phong
"""

ngay=int(input("nhap ngay"))
thang=int(input("nhap thang"))
nam=int(input("nhap nam"))
print(f"{ngay}/{thang}/{nam}")
print(f"{ngay}/{thang}/{str(nam)[-2:]}")
print(f"{nam}/{ngay}/{thang}")
ngay , thang , nam = map(int, input("nhap lai theo dinh dang ngay/thang/nam ").split('/'))
print(f"{ngay}/{thang}/{nam}")
print(f"{ngay}/{thang}/{str(nam)[-2:]}")
print(f"{nam}/{ngay}/{thang}")