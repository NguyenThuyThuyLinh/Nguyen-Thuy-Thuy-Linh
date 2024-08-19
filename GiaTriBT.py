# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:23:40 2024

@author: Nguyen Thuy Thuy Linh
"""
import math
a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
phan1 = (math.sqrt(a) - math.sqrt(b)) / (math.sqrt(math.sqrt(a)) - math.sqrt(math.sqrt(b)))
phan2 = (math.sqrt(a) + math.pow(a*b, 0.25)) / (math.sqrt(math.sqrt(a)) + math.sqrt(math.sqrt(b)))
result = phan1 - phan2
print(f"Kết quả: {result}")
if result == math.pow(b, 0.25):
    print(f"Kết quả đơn giản hóa: {result} = {math.pow(b, 0.25)}")
