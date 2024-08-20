# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:46:50 2024

@author: Student
"""
chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings_2 = chuoi.replace("P. ", "").replace("Q. ", "").replace("Tp. ", "").split(", ")

print("Tách thành các sub-string (theo yêu cầu 2):")
for sub in sub_strings_2:
    print(sub)