# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:54:03 2024

@author: Huynh Dieu My
"""
tg1 = input("Nhập vào thời gian thứ nhất (giờ,phút,giây): ")
tg2 = input("Nhập vào thời gian thứ hai: ")
h1, p1, s1 = map(int, tg1.split(','))
h2, p2, s2 = map(int, tg2.split(','))
tong1 = h1 * (60**2) + p1 *60 + s1
tong2 = h2 * (60**2) + p2 *60 + s2
hieu = tong1 - tong2
tong = tong1 + tong2 
tonggio = tong // 3600
tongphut = tong % 3600 // 60 
tonggiay = tong % 60
hieugio = hieu // 3600
hieuphut = hieu % 3600 // 60
hieugiay = hieu % 60
print("Tổng hai thời gian: ", tonggio, "giờ", tongphut, "phút", tonggiay, "giây")
print("Hiệu hai thời gian: ", hieugio, "giờ", hieuphut, "phút", hieugiay, "giây")

