#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 09:46:35 2022

@author: sangyoon
"""
import sys

N = int(sys.stdin.readline())

words = []

for _ in range(N):
    words.append(sys.stdin.readline())
    
words = list(set(words))
    
words.sort(key = lambda x : (len(x), x))

for i in words:
    print(i, end="")