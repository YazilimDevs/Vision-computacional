# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:53:58 2020

@author: pcardona
matplotlib: https://matplotlib.org/
cv2 : https://opencv.org/  
img_Color = mpimg.imread("img/image.jpg
numpy : https://numpy.org/
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2 


file_name = "img/image.jpg"


def fourChannels(img):
  height, width, channels = img.shape
  if channels < 4:
    new_img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    return new_img

  return img

def cut(img):
  # crop image
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
  morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

  cnts, _ = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnt = sorted(cnts, key=cv2.contourArea)[-1]
  x,y,w,h = cv2.boundingRect(cnt)
  new_img = img[y:y+h, x:x+w]

  return new_img  



def transBg(img):   
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
  morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)
  roi, _ = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  mask = np.zeros(img.shape, img.dtype)
  cv2.fillPoly(mask, roi, (255,)*img.shape[2], )
  masked_image = cv2.bitwise_and(img, mask)
  return masked_image



#Lee la imagen
img_Color = mpimg.imread("img/image.jpg")
img_Color = fourChannels(img_Color)
img_Color = cut(img_Color)
img_Color = transBg(img_Color)

cv2.imwrite("img/image_transparente.png", img_Color)
plt.imshow(img_Color)
img_Color.shape
