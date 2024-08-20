# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:30:38 2024

@author: Student
"""

chuoi = "I'm a cat"

chuoi_title = chuoi[0:4] + chuoi[4:].title()
print(chuoi_title)

chuoi_upper = chuoi.upper()
print(chuoi_upper)

chuoi_custom = chuoi[0:4].upper() + chuoi[4:7].lower() + chuoi[7:].swapcase()
print(chuoi_custom)

chuoi_mixed = chuoi.capitalize()
print(chuoi_mixed)