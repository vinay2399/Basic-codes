#simple linear regression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv('Salary_data.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values

#now split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)

#now fitting simple linear regression into testing data
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
y_pred=regressor.predict(x_test)

#visualising training set results
plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,regressor.predict(x_train),color='black')
plt.title('simple linear regression\n [salary vs employment - training set]')
plt.xlabel('year of employment')
plt.ylabel('salary')
plt.show()

#visualising test set results
plt.scatter(x_test,y_test,color='red')
plt.plot(x_test,regressor.predict(x_test),color='black')
plt.title('simple linear regression\n [salary vs employment - testing set]')
plt.xlabel('year of employment')
plt.ylabel('salary')
plt.show()