# -*- coding: utf-8 -*-
"""
Created on Tue May 24 09:42:45 2022

@author: SANTANU
"""
'''
import pywhatkit
pywhatkit.sendwhatmsg('', 'hi', 12, 15)

import random
import pyautogui as pg
import time
animal=('monkey','dog','cat')
time.sleep(8)
for i in range(10):
    a=random.choice(animal)
    pg.write('you are a ' + a)
    pg.press('enter')'''
from turtle import *
color('red')
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()
