# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:54:16 2024

@author: chillale sai krishna
"""

def div(n):   
    for i in range(0,n+1):
        if i%5 == 0 and i%7 == 0:
            yield i
            
            
            