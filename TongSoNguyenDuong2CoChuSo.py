# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:03:46 2024

@author: Nguyen Thuy Thuy Linh
"""
N = int(input("Nhập số nguyên dương N gồm 2 chữ số: "))
if 10 <= N <= 99:
                  print("Tổng các chữ số của N là:", (N // 10) + (N % 10))
else:
    print("Số nhập vào không phải là số nguyên dương có 2 chữ số.")
