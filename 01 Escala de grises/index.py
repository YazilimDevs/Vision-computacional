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

#Lee la imagen
img_Color = mpimg.imread("img/image.jpg")
#Muestra la imagen
plt.imshow(img_Color)
img_Color.shape

#Transforma la imagen a escala de grises
img_Gris = cv2.cvtColor(img_Color,  cv2.COLOR_BGR2GRAY)
plt.imshow(img_Gris, cmap='gray')

#Genera el archivo jpg de la imagen a escala de grises
cv2.imwrite("img/image_gray.jpg", img_Gris)