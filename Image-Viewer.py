# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:31:18 2019

@author: louis
"""

"""
"""
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mping
import numpy as np

#matplotlib.use('TkAgg'

#TODO 
def showimage1(imagefile):
    #print('hell from image1')
    status = 6  
    img=mping.imread(imagefile)
    #print (status+1)
    plt.imshow(img)
    plt.show()
    #print (status)
    return status

def showimage2(imagefile):
    status = 6  
    img=mping.imread(imagefile)
    #print (status+1)
    plt.imshow(img)
    plt.show()
    #print (status)
    return status

def showimage3(imagefile):
    status = 6  
    img=mping.imread(imagefile)
    #print (status+1)
    plt.imshow(img)
    plt.show()
    #print (status)
    return status

#main routine starts here
    
print ('Which Image would you like to view Image 1, 2 or 3: ')
image = int(input('1, 2, or 3'))
#print(image)
if image == 1:
    showimage1('images/image1.jpg')

    
if image == 2:
    showimage2('images/image2.jpg')

    
if image == 3:
    showimage3('images/image3.png')






#%matplotlib inline

#showimage1('images/image.jpg')

#img=mping.imread('images/image.jpg')
#img.view()

#print(img)

#plt.imshow(img)

#plt.show()
