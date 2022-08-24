# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 15:25:43 2022

@author: USER
"""

S = input().strip() 

ans1 = 0 
ans2 = 0 

cur = "0"

if S[0] == "0":
    ans1 += 1 
else:
    cur = "1"
    ans2 += 1

for i in S:
    if i != cur:
        if i == "0":
            ans1 += 1 
        else:
            ans2 += 1
        cur = i 
        
print(min(ans1, ans2))