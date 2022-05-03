# -*- coding: utf-8 -*-
"""
Created on Tue May  3 12:40:56 2022

@author: USER
"""

def solution(record):
    answer = []
    id_answer = []
    users = {}
    for i in record:
        l = i.split() 
        if l[0] == "Enter":
            users[l[1]] = l[2]
            id_answer.append((l[1],"님이 들어왔습니다."))
        elif l[0] == "Leave":
            id_answer.append((l[1],"님이 나갔습니다."))
        else:
            users[l[1]] = l[2]
    for i in id_answer:
        answer.append(users[i[0]]+i[1])
    return answer