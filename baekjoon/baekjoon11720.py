#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 17:10:09 2022

@author: sangyoon
"""

import sys 

_ = sys.stdin.readline()
nums = sys.stdin.readline()

s = 0
for num in nums[0:-1]:
    s += int(num)
    
print(s)