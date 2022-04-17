# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 21:32:56 2022

@author: USER
"""

def printStar(n):
    if n == 1:
        return "*"
    else:
        prev = printStar(n/3).split("\n")
        result = ""
        for i in prev:
            result += i * 3 + "\n"
        for i in prev:
            result += i + i.replace("*", " ") + i + "\n"
        for i in prev: 
            result += i * 3 + "\n"
        return result[:-1]
        
     
N = int(input())

print(printStar(N))