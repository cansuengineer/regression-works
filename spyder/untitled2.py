# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 01:08:52 2019

@author: Cansu
"""

import numpy as np
from sklearn.linear_model import LinearRegression

import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([35, 49, 21, 39, 15, 28]).reshape((-1, 1))
y = np.array([9, 15, 7, 11, 5, 8])

print (x)
print (y)

model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)

new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
print('intercept:', model.intercept_)
print('slope:', new_model.coef_)


y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

y_pred = model.intercept_ + model.coef_ * x
print('predicted response:', y_pred, sep='\n')