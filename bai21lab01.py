# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:34:17 2024

@author: Hoang Phong
"""


a = int(input("nhap 1 so nguyen "))
b = {
    0: "Khong",
    1: "Mot",
    2: "Hai",
    3: "Ba",
    4: "Bon",
    5: "Nam",
    6: "Sau",
    7: "Bay",
    8: "Tam",
    9: "Chin"
}
if a in b:
    print(b[a])
else:
    print("Khong doc duoc")
