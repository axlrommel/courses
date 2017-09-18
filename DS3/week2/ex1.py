from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

np.random.seed(0)
n = 15
x = np.linspace(0,10,n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10

X_train, X_test, y_train, y_test = train_test_split(x.reshape(-1, 1), y, random_state=0)
linreg = LinearRegression().fit(X_train, y_train)
degreeOne = list(map(lambda x: x * linreg.coef_[0] + linreg.intercept_,np.linspace(0,10,100) ))

X_F1_poly = PolynomialFeatures(degree=3).fit_transform(x.reshape(-1, 1))
X_train1, X_test1, y_train1, y_test1 = train_test_split(X_F1_poly, y, random_state = 0)
linreg = LinearRegression().fit(X_train1, y_train1)
degreeThree = list(map(lambda x: x * linreg.coef_[1] + x*x*linreg.coef_[2] + x*x*x*linreg.coef_[3] + linreg.intercept_,
    np.linspace(0,10,100) ))

X_F1_poly = PolynomialFeatures(degree=6).fit_transform(x.reshape(-1, 1))
X_train2, X_test2, y_train2, y_test2 = train_test_split(X_F1_poly, y, random_state = 0)
linreg = LinearRegression().fit(X_train2, y_train2)
degreeSix = list(map(lambda x: x * linreg.coef_[1] + x*x*linreg.coef_[2] + x*x*x*linreg.coef_[3] + 
    + x*x*x*x*linreg.coef_[4]  + x*x*x*x*x*linreg.coef_[5] + x*x*x*x*x*x*linreg.coef_[6] + linreg.intercept_,
    np.linspace(0,10,100) ))

plt.figure(figsize=(10,5))
plt.plot(X_train, y_train, 'o', label='training data', markersize=10)
plt.plot(X_test, y_test, 'o', label='test data', markersize=10)
#for i,degree in enumerate([1]):
plt.plot(np.linspace(0,10,100), np.array(degreeSix), alpha=0.8, lw=2, label='degree={}'.format("6"))
plt.plot(np.linspace(0,10,100), np.array(degreeThree), alpha=0.8, lw=2, label='degree={}'.format("3"))
plt.plot(np.linspace(0,10,100), np.array(degreeOne), alpha=0.8, lw=2, label='degree={}'.format("1"))
plt.ylim(-1,2.5)
plt.legend(loc=4)
plt.show()
    
    #return degreeOne