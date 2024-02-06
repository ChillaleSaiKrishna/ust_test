# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:27:29 2024

@author: chillale sai krishna
"""

# write a function that interleaves 2 strings


def myfunc(string_1,string_2):
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


string_1 = "AAAA"
string_2 = "1234567"

x = myfunc(string_1,string_2) # function call 

print("".join(x)) # join the result obtained
