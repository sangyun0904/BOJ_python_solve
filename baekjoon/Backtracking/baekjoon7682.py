#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:09:41 2022

@author: sangyoon
"""

import sys 
input = sys.stdin.readline 

def gameEnd(game):
    space = game.find(".")

    bingo = [game[:3], game[3:6], game[6:9], # row
             game[0]+game[3]+game[6], game[1]+game[4]+game[7], game[2]+game[5]+game[8], #col
             game[0]+game[4]+game[8], game[2]+game[4]+game[6] #cross
             ]
    
    if space == -1:
        return True
    elif "XXX" in bingo or "OOO" in bingo:
        return True
    else:
        return False
        
def Backtrack(game, start):
    
    while game != ".........":
        
    
        
while True:
    game = input().strip() 
    
    if game == "end":
        break
    
    x_cnt = game.count("X")
    o_cnt = game.count("O")
        
    if gameEnd(game) and 0 <= x_cnt - o_cnt < 2:
        is_valid = True
        
        if x_cnt - o_cnt == 1:
            Backtrack(game, "X")
        else:
            Backtrack(game, "O")
        
        print("valid")
    else:
        print("invalid")