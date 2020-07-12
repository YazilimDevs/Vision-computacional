# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:53:58 2020

@author: pcardona
matplotlib: https://matplotlib.org/
cv2 : https://opencv.org/
numpy : https://numpy.org

#Muestra la imagen
plt.imshow(img_Color)
img_Color.shape


"""


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2 

#Lee la imagen
img_Color = mpimg.imread("img/image.jpg")
#plt.imshow(img_Color, cmap='gray')

#Transforma la imagen a escala de grises
img_Gris = cv2.cvtColor(img_Color,  cv2.COLOR_BGR2GRAY)
#plt.imshow(img_Gris, cmap='gray')

#obtiene las esquinas de la imagen
corners = cv2.cornerHarris(img_Gris, 5,3, 0.1)
corners_dilate = cv2.dilate(corners, np.ones((8,8), np.uint8), iterations =1)
#plt.imshow(corners_dilate, cmap='gray')

#Copia la imagen de color ya que no la variable img_Color es solo para lectura
img_copy = img_Color.copy()
#Colorea de verde las esquinas detectadas 0,255,0, B,G,R para open cv
img_copy[corners_dilate > 0.01 * corners_dilate.max()] = [0,255,0];
plt.imshow(img_copy, cmap='gray')



