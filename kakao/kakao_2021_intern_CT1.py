#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 09:52:57 2022

@author: sangyoon
"""

line = input()

list_1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
list_2 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

def changeString(s):
    word = ""
    new_line = ""
    for i in s:
        word += i
        if word in list_1:
            new_line += word
            word = ""
        elif word in list_2:
            new_line += list_1[list_2.index(word)]
            word = ""
            
    print(new_line)
    
changeString(line)