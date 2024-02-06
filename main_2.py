# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:47:16 2024

@author: chillale sai krishna
"""

from Interleave import inter_string
import json 



def main():
    
    # Load data from Json file as inputs 
    with open("G:\Microsoft test\data.json", "r") as file:
        data = json.load(file)
    
    # interleave strings  
    x = inter_string(data["string_1"],data["string_2"]) # function call 
    print("".join(x))


if __name__ == "__main__":
    main()