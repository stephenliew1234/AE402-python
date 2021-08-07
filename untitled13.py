# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 09:41:45 2021

@author: stephen
"""

import random

n = random.randint(1, 20)

guess_count = 0

guess_limit = 5     #actual try count will be 3

while guess_count <= guess_limit :

    guess = int(input("Enter a number from 1 to 20: "))

    guess_count += 1
    
    if guess == n:

        print("you guessed it in ", guess_count,"Guesses")

        break
    
else:

    print ("The correct number is", n)