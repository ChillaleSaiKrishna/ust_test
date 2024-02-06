# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:10:58 2024

@author: chillale sai krishna
"""
#genrator function which gets values divisible by 5 or 7 for range 0 to n

def myfun(n):   
    for i in range(0,n+1):
        if i%5 == 0 or i%7 == 0:
            yield i
   
# input block         
n = int(input("enter any number: "))

# function call 
x = myfun(n)

# print the result in comma separated value 
for i in x:
    print(i, end=",")
    
    