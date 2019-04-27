# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:40:14 2018

The following program will simulate something that looks like "The Matrix" code. 
Note that dimensions might be different, so you might need to adjust. 
Speed can be adjusted with the time.sleep part and the symbols displayed can 
also be customized. 
For better results, run in command prompt! 

Have fun! 

@author: jairp
"""

import random as r
import time 
import string

spaces = " "*8 
letters = string.ascii_letters + string.digits + string.hexdigits + spaces 
rand_letters = r.choices(letters, k = 200) # choose 200 random symbols from here

# ****************************

symbols = ["0","1"," ", " "] # can choose from these symbols if wanted 

line = [] # empty list 
counter = 0
    
# create first line 

for i in range(119):  # animation length
    x = r.randint(0,199)
    line.append(rand_letters[x])
    
    counter += 1

print(*line)

for i in range(10000): # animation 10000 lines long  
    
    # change 10 characters every fifth time 
    if counter % 1 == 0: 
        r_symbols  = [r.randint(0, 118) for x in range (118)]
        
        for i in r_symbols :
            line[i]  = rand_letters[r.randint(0,118)]

    print(*line)
    counter += 1
    time.sleep(0.05)    # pause every 0.05 seconds      

