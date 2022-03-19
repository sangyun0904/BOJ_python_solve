#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:31:46 2022

@author: sangyoon
"""

import sys 

house, router = map(int, sys.stdin.readline().split())

house_list = []

for _ in house:
    house_list.append(int(sys.stdin.readline()))
    
house_list.sort()

