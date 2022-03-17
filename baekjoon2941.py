#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:55:21 2022

@author: sangyoon
"""

import sys 

word = sys.stdin.readline()[0:-1]

croatia_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatia_alphabets:
    if i in word:
        word = word.replace(i, "?")
        
print(len(word))