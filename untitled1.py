# -*- coding: utf-8 -*-
"""
Created on Sat May 21 01:15:30 2022

@author: SANTANU
"""

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
n_samples = 1500
random_state = 170
X, y = make_blobs(n_samples=n_samples, random_state=random_state)
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X)
plt.figure(figsize=(6, 6))
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("K-Means Clustering")