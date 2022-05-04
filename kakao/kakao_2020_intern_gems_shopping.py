#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 19:54:52 2022

@author: sangyoon
"""

def solution(gems):
    answer = []
    n = len(set(gems))
    s = 0
    e = -1 
    d = {}
    dist = int(1e9)
    while e < len(gems)-1:
        e += 1
        if gems[e] in d:
            d[gems[e]] += 1
        else:
            d[gems[e]] = 1 
        
        while len(d) == n:
            if d[gems[s]] == 1:
                del d[gems[s]]
                if (e - s) < dist:
                    dist = (e - s)
                    answer = [s+1, e+1]
            else:
                d[gems[s]] -= 1
            s += 1
        
    return answer