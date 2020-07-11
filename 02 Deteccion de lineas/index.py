# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:53:58 2020

@author: pcardona

matplotlib: https://matplotlib.org/
cv2 : https://opencv.org/
numpy : https://numpy.org/

"""


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2 

#img_Color = mpimg.imread("img/image.jpg")
img_Color = mpimg.imread("img/image2.jpg")
#plt.imshow(img_Color)
img_Color.shape

img_Gris = cv2.cvtColor(img_Color,  cv2.COLOR_BGR2GRAY)
#plt.imshow(img_Gris, cmap='gray')
img_Gris.shape

img_Copia = np.copy(img_Gris)
img_Copia[(img_Copia[:,:]<250)]=0
plt.imshow(img_Copia, cmap="gray")
plt.show()