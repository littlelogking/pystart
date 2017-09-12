#
"""
Created on Tue Sep 12 18:13:36 2017

@author: louis
"""

#This program will draw an alien

from Tkinter import *

window=Tk()
window.title('Alien')

c = Canvas(window, height=300, width=400)
c.pack()

body = c.create_oval(100, 150, 300, 250, fill='green')

eye = c.create_oval(170, 70, 230, 130, fill='black')

eyeball = c.create_oval(190, 90, 210, 110,fill='blue')

mouth = c.create_oval(150, 220, 250, 240, fill='black')

neck = c.create_line(200, 150, 200, 130)

hat = c.create_polygon(180, 75, 220, 75, 200, 20, fill='red')

window.mainloop(0)
#you can change the colours by changing fill='blue'or whatever the colour is 
#this was from a book by carrel vordeman 
#this program dosn't work till finished  