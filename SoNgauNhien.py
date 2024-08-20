# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:03:19 2024

@author: Nguyen Thuy Thuy Linh
"""

import random

def random_number_in_range(start, end):
    return random.randint(start, end)

start = 10
end = 100

print(f"Số ngẫu nhiên trong đoạn [{start}, {end}]:", random_number_in_range(start, end))