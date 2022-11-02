# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:51:50 2022

@author: SANTANU
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
ir = pd.read_csv('irise.csv')
X = ir.drop(columns=['variety'])
y = ir['variety']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
score = accuracy_score(y_test, prediction)


