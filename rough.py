# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 07:39:51 2022

@author: SANTANU
"""
import matplotlib.pyplot as plt
import cv2

plt.figure(figsize=(5,5))
imgGray = cv2.imread('data/image.jpg')
gray = cv2.cvtColor(imgGray,cv2.COLOR_RGB2GRAY)
plt.imshow(gray, cmap="gray")
# plt.show()

plt.hist(imgGray.ravel(),256,[0,256],color='violet')
# plt.show()

equi = cv2.equalizeHist(gray)
plt.imshow(equi,cmap="gray")
# plt.show()

plt.hist(equi.flatten(),bins=256,color='b')
# plt.show()



a=plt.subplot(2,2,1)
a.set_title("Original Image")
plt.imshow(gray,cmap="gray")

b=plt.subplot(2,2,2)
plt.hist(gray.flatten(),bins=256,color="blue")
b.set_title("Original Image")

c=plt.subplot(2,2,3)
c.set_title("Equalised Image")
plt.imshow(equi,cmap="gray")

d=plt.subplot(2,2,4)
plt.hist(equi.flatten(),bins=256,color="blue")
d.set_title("Equalised Image")
plt.show()

