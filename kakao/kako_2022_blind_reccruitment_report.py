#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 22:48:42 2022

@author: sangyoon
"""

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2


def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    user_report = [[] for _ in range(len(id_list))]
    report = list(set(report))
    for r in report:
        r = r.split()
        user_report[id_list.index(r[0])].append(r[1])
    rejected = [False for _ in range(len(id_list))]
    for i in range(len(id_list)):
        cnt = 0 
        for j in range(len(id_list)):
            if id_list[i] in user_report[j]:
                cnt += 1 
                if cnt == k:
                    rejected[i] = True
                    break
    for i in range(len(user_report)):
        for j in user_report[i]:
            if rejected[id_list.index(j)]:
                answer[i] += 1
        
    return answer

print(solution(id_list, report, k))