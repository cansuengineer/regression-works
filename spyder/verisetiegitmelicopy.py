# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 23:54:29 2019

@author: Cansu
"""

import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_excel("datalar.xlsx")

X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,1].values

from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=1/3,random_state=0)

from sklearn.linear_model import LinearRegression
simplelinearRegression=LinearRegression()
simplelinearRegression.fit(X_train,Y_train)

Y_predict=simplelinearRegression.predict(X_test)

plt.scatter(X_train,Y_train,color='red')
plt.plot(X_train,simplelinearRegression.predict(X_train))
plt.show()

