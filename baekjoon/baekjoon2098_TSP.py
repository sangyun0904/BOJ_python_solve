#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 13:06:36 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

N = int(input())

dist = []
for _ in range(N):
    dist.append(list(map(int, input().split())))
    
def 