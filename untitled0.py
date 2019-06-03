# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:36:27 2019

@author: suilven
"""
#these are imports
#I make images using tkinter
from tkinter import *

#this gets window ready
window=Tk()
window.title('Animation')

c = Canvas(window, height=1000, width=900)
c.pack()

#this makes alien
head = c.create_oval(100, 150, 300, 250, fill='green')

eye = c.create_oval(170, 70, 230, 130, fill='blue')

eyeball = c.create_oval(190, 90, 210, 110,fill='blue')

mouth = c.create_oval(150, 220, 250, 240, fill='red')

neck = c.create_line(200, 150, 200, 130)

hat = c.create_polygon(180, 75, 220, 75, 200, 20, fill='red')

body = c.create_rectangle(150, 220, 250, 240, 150, 300, 250, 300, fill='green')

window.mainloop(0)

