#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 19:43:58 2022

@author: sangyoon
"""

line = input()

s = line.split("-")

ans = sum(map(int, s[0].split("+")))

for i in s[1:]:
    ans -= sum(map(int, i.split("+")))
    
print(ans)