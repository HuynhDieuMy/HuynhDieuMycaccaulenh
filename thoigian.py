# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:37:43 2024

@author: Huynh Dieu My
"""

thoigian = input("Nhập thời gian hh:mm:ss: ")
hh,mm,ss = map(int,thoigian.split(':'))
print("Thời gian sau khi đổi ra giây: ", hh*60*60 + mm*60 +ss)