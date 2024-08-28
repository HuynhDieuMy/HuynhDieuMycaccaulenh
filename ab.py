# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:28:21 2024

@author: Huynh Dieu My
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
a1 = a**(1/3)
b1 = b**(1/3)
c = (a*b)**(1/3)
print("Kết quả của biểu thức: ", (((a+b)/(a1+b1))-c) / ((a1 - b1)**2))