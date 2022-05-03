# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:26:12 2022

@author: USER
"""

from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        cnts = {}
        for o in orders:
            for i in list(combinations(o, c)):
                i = "".join(sorted(list(i)))
                if i in cnts.keys():
                    cnts[i] += 1
                else:
                    cnts[i] = 1
        for k, v in cnts.items():
            if v == max(cnts.values()) and v != 1:
                answer.append(k)
                
    answer.sort()
    return answer