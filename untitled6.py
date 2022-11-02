# -*- coding: utf-8 -*-
"""
Created on Tue May 24 10:34:57 2022

@author: SANTANU
"""

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
imgray = cv2.convertScaleAbs(imgray, alpha=1.10, beta=-20)
cv2.imshow('binary', imgray)
cv2.waitKey(0)


