#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:25:47 2020

@author: vickysharma
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Position_Salaries.csv')

X=df.iloc[:,1:2].values
Y=df.iloc[:,2].values

from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=10,random_state=0)
regressor.fit(X,Y)

y_pred=regressor.predict(np.array([6.5]).reshape(1,1))

x_grid=np.arange(min(X),max(X),0.01)
x_grid=x_grid.reshape((len(x_grid),1))
plt.scatter(X,Y,color='red')
plt.plot(x_grid,regressor.predict(x_grid),color='blue')
plt.title('Truth or Bluff (Random Forest Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()