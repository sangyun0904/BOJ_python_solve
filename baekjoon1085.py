#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:48:58 2022

@author: sangyoon
"""

import sys 

x, y, w, h = map(int, sys.stdin.readline().split())

dist_list = [x, y, w-x, h-y]

print(min(dist_list))