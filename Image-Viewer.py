# -*- coding: utf-8 -*-
"""
Created on Fri May 10 07:09:47 2019

@author: suilven
"""

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mping
import numpy as np
import sys




#matplotlib.use('TkAgg'

#TODO 
def showimage(imagefile):
    #print('hell from image1')
    status = 6  
    img=mping.imread(imagefile)
    #print (status+1)
    plt.imshow(img)
    plt.show()
    #print (status)
    return status

def stop():
    status=0
    print("Goodbye")
    sys.exit(0)
    
    return status
    


#main routine starts here
    
print ('Which Image would you like to view Image 1, 2 or 3: ')
image = (input('1, 2, 3 or none'))
#print(image)
if image == '1':
    showimage('images/image1.jpg')
    stop()

    
if image == '2':
    showimage('images/image2.jpg')
    stop()

    
if image == '3':
    showimage('images/image3.png')
    stop()
    








#%matplotlib inline

#showimage1('images/image.jpg')

#img=mping.imread('images/image.jpg')
#img.view()

#print(img)

#plt.imshow(img)

#plt.show()