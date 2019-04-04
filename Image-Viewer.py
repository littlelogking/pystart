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

#matplotlib.use('TkAgg')




def showimage(imagefile):
    status = 6  
    img=mping.imread(imagefile)
    print (status+1)
    plt.imshow(img)
    plt.show()
    print (status)
    return status
              


print(matplotlib.get_backend())
#%matplotlib inline

showimage('images/image.jpg')

#img=mping.imread('images/image.jpg')
#img.view()

#print(img)

#plt.imshow(img)

#plt.show()
