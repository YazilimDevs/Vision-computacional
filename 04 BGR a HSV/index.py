# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:53:58 2020

@author: pcardona
"""


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2 

img_Color = mpimg.imread("img/image.jpg")
img_Color.shape

print('Altura: ', int(img_Color.shape[0]),'pixeles')
print('Anchura: ', int(img_Color.shape[1]),'pixeles')

"Visualiza la imagen con Open cv"
cv2.imshow('hola sonia',img_Color)
cv2.waitKey()
cv2.destroyAllWindows()

"Visualiza la imagen con pyplot"
plt.imshow(img_Color)
img_Color.shape

"Convierte la imagen a escala de grises"
img_gris = cv2.cvtColor(img_Color, cv2.COLOR_BGR2GRAY)
cv2.imshow('hola sonia',img_gris)
cv2.waitKey()
cv2.destroyAllWindows()

"Convierte la imagen a escala de grises"
img_HSV = cv2.cvtColor(img_Color, cv2.COLOR_BGR2HSV )
cv2.imshow('hola sonia',img_HSV)
cv2.waitKey()
cv2.destroyAllWindows()

B,G,R = cv2.split(img_Color)

"Convierte la imagen a escala de grises"
cv2.imshow('hola sonia',B)
cv2.waitKey(0)
cv2.destroyAllWindows()


"Convierte la imagen a azul"
zeros =  np.zeros(img_Color.shape[:2], dtype="uint8")
cv2.imshow('hola sonia',cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()


img_merged = cv2.merge([B,G,R])
cv2.imshow('hola sonia',img_merged)


















