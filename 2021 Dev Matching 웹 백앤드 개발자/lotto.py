#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 14:54:51 2022

@author: sangyoon
"""

def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zeros = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            cnt += 1
    if cnt > 1:
        answer = [7-cnt-zeros, 7-cnt]
    else:
        if zeros + cnt > 1:
            answer = [7-zeros-cnt, 6]
        else:
            answer = [6,6]
    return answer