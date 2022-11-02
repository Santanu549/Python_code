# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:39:40 2022

@author: SANTANU
"""

import numpy as np
import random
mu, sigma = 0, 10
s = np.random.normal(mu, sigma, 1000)
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 20, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=0, color='k')
plt.title('NORMAL DISTRIBUTION')
plt.xlabel('Z-score')
plt.ylabel('Probablity Density')
plt.show()
    