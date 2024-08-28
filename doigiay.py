# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:34:40 2024

@author: Huynh Dieu My
"""

giophutgiay = input("Nhập thời gian giờ (h), phút (p), giây (s): ")
so = ""
for i in giophutgiay:
    if i.isalpha():
        so += ":"
    else:
        so += i
sosau = so[:-1]
h, p, s = map(int, sosau.split(':'))
tonggiay = h * 3600 + p* 60 + s 
print("Tổng số giây: ", tonggiay)