#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:14:17 2022

@author: sangyoon
"""

def parse_expr(expStr):
    tokens = [x for x in expStr]
    op = dict(zip('*/+-()', (50, 50, 40, 40, 0, 0)))
    output = []
    stack = []
    
    for item in tokens:
        if item not in op:
            output.append(item)
        elif item == '(':
            stack.append(item)
        elif item == ')':
            while stack != []] and 
                  stack[-1] != '(':
                

def calc_expr(expStr):
    tokens = parse_expr(expStr)