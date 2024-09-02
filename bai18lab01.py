# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:36:51 2024

@author: Hoang Phong
"""

gio1=int(input("nhap gio mot:"))
gio2 = int(input("nhap gio hai: "))
phut1 = int(input("nhap phut mot: "))
phut2 = int(input("nhap phut hai: "))
giay1 = int(input("nhap giay mot: "))
giay2 = int(input("nhap giay hai: "))
gio_cong_gio = gio1 + gio2
gio_tru_gio = gio1 - gio2
phut_cong_phut = phut1 + phut2
phut_tru_phut = phut1 - phut2
giay_cong_giay = giay1 + giay2
giay_tru_giay = giay1 - giay2
print(f"ket qua cong:gio {gio_cong_gio}, phut {phut_cong_phut}, giay {giay_cong_giay}")
print(f"ket qua tru : gio {gio_tru_gio},phut{phut_tru_phut},giay{giay_tru_giay}")
