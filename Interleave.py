# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:03:42 2024

@author: chillale sai krishna
"""

# genrator function which gets values divisible by 5 or 7 for range 0 to n



def inter_string(string_1,string_2):
    for i,j in zip(string_1,string_2):    # it iterates simultaniously between two strings
        yield i
        yield j
   
   # get rest of the string      
    if len(string_1) > len(string_2):
        for k in string_1[len(string_2):]:
            yield k
            
    if len(string_2) > len(string_1):
        for k in string_2[len(string_1):]:
            yield k
            