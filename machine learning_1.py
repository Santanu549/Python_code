# -*- coding: utf-8 -*-
"""
Created on Thu May 19 02:21:19 2022

@author: SANTANU
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
ir = pd.read_csv('irise.csv')
X = ir.drop(columns=['variety'])
y = ir['variety']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
model = MLPClassifier(max_iter=1000)
model.fit(X_train, y_train)
prediction = model.predict(X_test)
score = accuracy_score(y_test, prediction)
print(score)