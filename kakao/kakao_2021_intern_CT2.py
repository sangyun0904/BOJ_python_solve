#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:14:48 2022

@author: sangyoon
"""

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], 
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


def bfs(place, current):  
    queue1 = []
    x1, y1 = current
    
    m = 5
    n = 5
    
    if x1 > 0:
        if place[x1-1][y1] != "X":
            queue1.append((x1-1, y1))
    if y1 > 0:
        if place[x1][y1-1] != "X":
            queue1.append((x1, y1-1))
    if x1 < n-1:
        if place[x1+1][y1] != "X":
            queue1.append((x1+1, y1))
    if y1 < m-1:
        if place[x1][y1+1] != "X":
            queue1.append((x1, y1+1))
        
    for a, b in queue1:
        if place[a][b] == "P":
            return False
    
    queue2 = []
    
    for x, y in queue1:
    
        if x > 0:
            if place[x-1][y] != "X":
                queue2.append((x-1, y))
        if y > 0:
            if place[x][y-1] != "X":
                queue2.append((x, y-1))
        if x < n-1:
            if place[x+1][y] != "X":
                queue2.append((x+1, y))
        if y < m-1:
            if place[x][y+1] != "X":
                queue2.append((x, y+1))
            
    for a, b in queue1:
        if place[a][b] == "P":
            return False
        
    return True
            
def loop_sits(place):
    for y in  range(5):
        for x in range(5):
            if place[x][y] == "P":
                if not bfs(place, (x, y)):
                    return False         
    return True
                
        
for i in places:
    if loop_sits(i):
        print(1, end=" ")
    else:
        print(0, end=" ")
        
    
    