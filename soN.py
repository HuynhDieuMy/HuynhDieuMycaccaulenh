# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:32:39 2024

@author: Huynh Dieu My
"""

N = int(input("Nhập số dương N: "))
if N<10 or N>99:
    print("Số N phải là số có 2 chữ số!")
else:
    hangchuc =  N//10
    hangdonvi =  N%10
print("Tổng 2 số của N: ", hangchuc + hangdonvi)