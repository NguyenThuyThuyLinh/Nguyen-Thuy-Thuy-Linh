# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:41:45 2024

@author: Nguyen Thuy Thuy Linh
"""

chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings_1 = chuoi.split(", ")

print("Tách thành các sub-string (theo yêu cầu 1):")
for sub in sub_strings_1:
    print(sub)
