# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:09:45 2022

@author: USER
"""

N = int(input()) 

cnt = 1
step = 0

while True:
    step += cnt
    if step >= N:
        break
    cnt += 1
    
if cnt % 2 == 0:
    print(cnt - step + N, "/", step - N + 1, sep="")
else:
    print(step - N + 1, "/", cnt - step + N, sep="")