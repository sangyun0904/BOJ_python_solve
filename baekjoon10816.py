#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:37:10 2022

@author: sangyoon
"""

filename = "baekjoon10816.txt"
file1 = open(filename, 'r')

n = int(file1.readline())
numList = list(map(int, file1.readline().split()))
        
m = int(file1.readline())
checkList = list(map(int, file1.readline().split()))

numDict = {}

for num in checkList:
    numDict[num] = 0

checkList.sort()

for num in numList:
    start = 0
    end = len(checkList) - 1
    while start <= end:
        mid = (start + end) // 2
        if checkList[mid] == num:
            numDict[num] += 1
            break
        elif checkList[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    
for i in numDict.values():
    print(i, end=" ")