# -*- coding: utf-8 -*-
"""
Created on Sat May 21 01:37:36 2022

@author: SANTANU
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
df = pd.read_csv('Book2.csv')
reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area, df.price, color='red', marker='+')
plt.plot(df.area, reg.predict(df[['area']]), color='blue')

