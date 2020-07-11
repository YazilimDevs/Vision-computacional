# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:53:58 2020

@author: pcardona
"""


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2 

#img_Color = mpimg.imread("img/image.jpg")
img_Color = mpimg.imread("img/image2.jpg")
"plt.imshow(img_Color)"
img_Color.shape



img_Copia = np.copy(img_Color)
img_Copia.shape
"[R:,G :,B]"
"[ :,  :,0] "
img_Copia[(img_Copia[:,:,0]<200)|(img_Copia[:,:,1]<200)|(img_Copia[:,:,2]<200)]=0
plt.imshow(img_Copia, cmap="gray")
plt.show()