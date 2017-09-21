# ### Question 1
# 
# Write a function that fits a polynomial LinearRegression model on the *training data* `X_train` for degrees 1, 3, 6, and 9. (Use PolynomialFeatures in sklearn.preprocessing to create the polynomial features and then fit a linear regression model) For each model, find 100 predicted values over the interval x = 0 to 10 (e.g. `np.linspace(0,10,100)`) and store this in a numpy array. The first row of this array should correspond to the output from the model trained on degree 1, the second row degree 3, the third row degree 6, and the fourth row degree 9.
# 
# <img src="polynomialreg1.png" style="width: 1000px;"/>
# 
# The figure above shows the fitted models plotted on top of the original data (using `plot_one()`).
# 
# <br>
# *This function should return a numpy array with shape `(4, 100)`*

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
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
degreeThree = list(map(lambda x: x * linreg.coef_[1] + x**2*linreg.coef_[2] + x**3*linreg.coef_[3] + linreg.intercept_,
    np.linspace(0,10,100) ))

X_F1_poly = PolynomialFeatures(degree=6).fit_transform(x.reshape(-1, 1))
X_train2, X_test2, y_train2, y_test2 = train_test_split(X_F1_poly, y, random_state = 0)
linreg = LinearRegression().fit(X_train2, y_train2)
degreeSix = list(map(lambda x: x * linreg.coef_[1] + x**2*linreg.coef_[2] + x**3*linreg.coef_[3] +
    x**4*linreg.coef_[4]  + x**5*linreg.coef_[5] + x**6*linreg.coef_[6] + linreg.intercept_,
    np.linspace(0,10,100) ))

X_F1_poly = PolynomialFeatures(degree=9).fit_transform(x.reshape(-1, 1))
X_train3, X_test3, y_train3, y_test3 = train_test_split(X_F1_poly, y, random_state = 0)
linreg = LinearRegression().fit(X_train3, y_train3)
degreeNine = list(map(lambda x: x * linreg.coef_[1] + x**2*linreg.coef_[2] + x**3*linreg.coef_[3] +
    x**4*linreg.coef_[4]  + x**5*linreg.coef_[5] + x**6*linreg.coef_[6] + 
    x**7*linreg.coef_[7]  + x**8*linreg.coef_[8] + x**9*linreg.coef_[9] + linreg.intercept_,
    np.linspace(0,10,100) ))

plt.figure(figsize=(10,5))
plt.plot(X_train, y_train, 'o', label='training data', markersize=10)
plt.plot(X_test, y_test, 'o', label='test data', markersize=10)
#for i,degree in enumerate([1]):
plt.plot(np.linspace(0,10,100), np.array(degreeNine), alpha=0.8, lw=2, label='degree={}'.format("9"))
plt.plot(np.linspace(0,10,100), np.array(degreeSix), alpha=0.8, lw=2, label='degree={}'.format("6"))
plt.plot(np.linspace(0,10,100), np.array(degreeThree), alpha=0.8, lw=2, label='degree={}'.format("3"))
plt.plot(np.linspace(0,10,100), np.array(degreeOne), alpha=0.8, lw=2, label='degree={}'.format("1"))
plt.ylim(-1,2.5)
plt.legend(loc=4)
plt.show()
    
    #return degreeOne