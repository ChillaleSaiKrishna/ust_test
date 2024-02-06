# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:46:33 2024

@author: chillale sai krishna
"""

from divisible import div
import json 



def main():
    
    # Load data from Json file as inputs 
    with open("G:\Microsoft test\data.json", "r") as file:
        data = json.load(file)
    
    # divisible by 5 or 7 
    x = div(int(data["n"])) 
    print(*(i for i in x), sep=",")
    

if __name__ == "__main__":
    main()