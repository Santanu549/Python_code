# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:08:06 2022

@author: SANTANU
"""


#important library to show the image 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#importing numpy to work with large set of data.
import numpy as np
#image read function
img=mpimg.imread('aliah.png')
#image sclicing into 2D. 
x=img[:,:,0]
# x co-ordinate denotation. 
plt.xlabel("Value")
# y co-ordinate denotation.
plt.ylabel("pixels Frequency")
# title of an image .
plt.title("Original Image")
# imshow function with comperision of gray level value.
plt.imshow(x,cmap="gray")
#plot the image on a plane.
plt.show()
plt.title("HIstogramm for given Image'  ")
plt.xlabel("Value")
plt.ylabel("pixels Frequency")
#hist function is used to plot the histogram of an image.
plt.hist(x)
histogram, bin_edges = np.histogram(img, bins=10, range=(0, 1))
# configure and draw the histogram figure
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.xlim([0.0, 1.0])  # <- named arguments do not work here

plt.plot(bin_edges[0:-1], histogram)  # <- or here
plt.show()

import cv2 as cv
b, g, r=cv.split(img)

cv.imshow("img", img)
cv.imshow("b", b)
plt.hist(img.ravel(), 256, [0,256])
plt.hist(b.ravel(), 256, [0,256])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
