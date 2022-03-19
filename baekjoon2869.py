#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:07:10 2022

@author: sangyoon
"""

import sys 

A, B, V = map(int, sys.stdin.readline().split())

if (V - A) % (A - B) == 0: 
    day = (V - A) // (A - B) + 1
else:
    day = (V - A) // (A - B) + 2
    
print(day)