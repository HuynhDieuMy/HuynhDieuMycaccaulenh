# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:30:14 2024

@author: Huynh Dieu My
"""

ngaythangnam = input("Nhập vào ngày tháng năm: ")
dd,mm,yyyy = ngaythangnam.split(' ')
print("Ngày/Tháng/Năm: ", dd,"/",mm,"/",yyyy)
print("Ngày/Tháng/Năm: ", dd,"/",mm,"/",yyyy[2:])
print("Năm/Tháng/Ngày: ", yyyy,"/",mm,"/",dd)