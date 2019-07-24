# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:36:27 2019

@author: suilven
"""
#these are imports
#I make images using tkinter
#from tkinter import *
import tkinter as tk
import math
import os
from PIL import Image
from PIL import ImageDraw

#this gets window ready
window=tk.Tk()
window.title('Animation')

iwidth = 900
iheight = 1000

c = tk.Canvas(window, height=iheight, width=iwidth)
c.pack()

image1 = Image.new("RGB", (iwidth, iheight), 'white')



#this makes alien
str1 = "alien"
#draw.text((10, 20), str1, 'black')
#draw.ellipse([100, 150, 300, 250],'black')
#draw.line([50,50,100,100],'black')

for i in range(1,4):
    draw = ImageDraw.Draw(image1)
    draw.line([50+i*10,50,100,100],'blue')
#for i in range(1,4):
    draw.text((10, 20), str1, 'black')
    draw.ellipse([100+i*10, 150, 300+i*10, 250],'green')
    #draw.line([50+i*10,50,100,100],'black')
    filename = "animation/does_it_work"+str(i)+".jpg"
    image1.save(filename)  
    del draw

#ffmpeg documentation https://ffmpeg.org/ffmpeg.html#Examples-1
#ffmpeg command    
#ffmpeg -f image2 -framerate 12 -i foo-%03d.jpeg -s WxH foo.avi
#ffmpeg -f image2 -framerate 12 -i does_it_work%d.jpg foo.avi

