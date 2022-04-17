#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:43:55 2022

@author: sangyoon
"""
import sys

n1, n2 = sys.stdin.readline().strip().split()

n1 = int(n1[2] + n1[1] + n1[0])
n2 = int(n2[2] + n2[1] + n2[0])

if n1 > n2:
    print(n1)
else:
    print(n2)