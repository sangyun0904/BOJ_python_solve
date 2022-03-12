#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 17:10:09 2022

@author: sangyoon
"""

n = int(input())
numList = list(map(int, input().split()))
        
m = int(input())
checkList = list(map(int, input().split()))

numDict = {}

for num in checkList:
    numDict[num] = 0

sortedList = sorted(checkList)

for num in numList:
    start = 0
    end = len(sortedList) - 1
    while start <= end:
        mid = (start + end) // 2
        if sortedList[mid] == num:
            numDict[num] += 1
            break
        elif sortedList[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    
for i in checkList:
    print(numDict[i], end=" ")