# -*- coding: utf-8 -*-
"""
Created on Tue May 28 07:43:16 2019

@author: suilven
"""
# PIL image, draw, line (draws in memory, but can be saved in many formats)
# Python Image Library (PIL) free from:
# http://www.pythonware.com/products/pil/index.htm

import tkinter as tk
import math
import os
from PIL import Image
from PIL import ImageDraw

blue = (255, 255, 255)
blue = (0, 0, 0)
blue = (0, 0, 255)
blue = (255, 0, 0)
blue = (0,128,0)

root = tk.Tk()
root.title("Simple plot using canvas and line")

width = 400
height = 300
center = height//2
x_increment = 1
x_factor = 0.04
y_amplitude = 80

cv = tk.Canvas(width=width, height=height, bg='white')
cv.pack()

image1 = Image.new("RGB", (width, height), 'white')
draw = ImageDraw.Draw(image1)

sine_list = []
for x in range(400):
    sine_list.append(x * x_increment)
    sine_list.append(int(math.sin(x * x_factor) * y_amplitude) + center)

cos_list = []
for x in range(400):
    cos_list.append(x * x_increment)
    cos_list.append(int(math.cos(x * x_factor) * y_amplitude) + center)

str1 = "sin(x)=blue  cos(x)=red"
cv.create_text(10, 20, anchor='sw', text=str1)
center_line = cv.create_line([0, center, width, center], fill='green')
sin_line = cv.create_line(sine_list, fill='blue')
cos_line = cv.create_line(cos_list, fill='red')

cv.postscript(file="my_drawing.ps", colormode='color')

draw.text((10, 20), str1, 'black')
draw.line([0, center, width, center], 'green')
draw.line(sine_list, 'blue')
draw.line(cos_list, 'red')


for i in range(1,4):
    filename = "animation/does_it_work"+str(i)+".jpg"
    image1.save(filename)

