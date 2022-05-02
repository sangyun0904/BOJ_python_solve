#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:05:53 2022

@author: sangyoon
"""

def solution(numbers, hand):
    answer = ''
    L = [0,3]
    R = [2,3]
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += "L"
            L = [0,i//3]
        elif i == 3 or i == 6 or i == 9:
            answer += "R"
            R = [2, i//3-1]
        elif i == 2 or i == 5 or i == 8:
            if abs(L[0]-1) + abs(L[1]-i//3) < abs(R[0]-1) + abs(R[1]-i//3) :
                answer += "L"
                L = [1, i//3]
            elif abs(L[0]-1) + abs(L[1]-i//3) > abs(R[0]-1) + abs(R[1]-i//3) :
                answer += "R"
                R = [1, i//3]
            else:
                if hand == "left":
                    answer += "L"
                    L = [1, i//3]
                else:
                    answer += "R"
                    R = [1, i//3]
        else:
            if abs(L[0]-1) + abs(L[1]-3) < abs(R[0]-1) + abs(R[1]-3):
                answer += "L"
                L = [1,3]
            elif abs(L[0]-1) + abs(L[1]-3) > abs(R[0]-1) + abs(R[1]-3):
                answer += "R"
                R = [1,3]
            else:
                if hand == "left":
                    answer += "L"
                    L = [1,3]
                else:
                    answer += "R"
                    R = [1,3]
            
    return answer