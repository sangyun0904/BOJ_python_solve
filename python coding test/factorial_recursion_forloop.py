#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 15:17:19 2022

@author: sangyoon
"""
import time

n = 2000

def factorial_recursion(x):
    if x > 0:
        return x * factorial_recursion(x-1)
    else:
        return 1
    
def factorial_loop(x):
    result = 1 
    for i in range(2, x + 1):
        result = result * i
    return result


recur_start = time.time()
factorial_recursion(n)
recur_end = time.time()
recur_delta = recur_end - recur_start

print("Recursion DeltaT %2.9f sec" % recur_delta)

loop_start = time.time()
factorial_loop(n)
loop_end = time.time()
loop_delta = loop_end - loop_start

print("Loop DeltaT %2.9f sec" % loop_delta)
        