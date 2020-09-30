# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:13:28 2020

@author: user
"""
import random

r = random.randint(1, 100)



while Truee :
    num = input('請輸入數字: ')
    num = int(num)
    if num == r :
        print('u got it')
        break
    elif num > r :
        print ('比答案大')
    elif num < r :
        print ('比答案小')