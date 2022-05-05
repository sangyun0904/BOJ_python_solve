# -*- coding: utf-8 -*-
"""
Created on Thu May  5 22:11:37 2022

@author: USER
"""
from itertools import permutations

def isBan(users, banned_id):
    for i in range(len(users)):
        user = users[i]
        ban = banned_id[i]
        if len(user) != len(ban):
            return False 
        for j in range(len(user)):
            if ban[j] != "*":
                if ban[j] != user[j]:
                    return False
    return True

def solution(user_id, banned_id):
    answer = []
    n = len(banned_id)
    users_list = permutations(user_id, n)
    for users in users_list:
        if isBan(users, banned_id):
            users = set(users)
            if users not in answer:
                answer.append(users)
    return len(answer)