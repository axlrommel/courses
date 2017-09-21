# Training models on high degree polynomial features can result in overly complex models that overfit, 
# so we often use regularized versions of the model to constrain model complexity, 
# as we saw with Ridge and Lasso linear regression.
# For this question, train two models: a non-regularized LinearRegression model 
# (default parameters) and a regularized Lasso Regression model (with parameters  alpha=0.01, max_iter=10000) 
# on polynomial features of degree 12. Return the  R2R2  score for both the LinearRegression and Lasso model's 
# test sets.
# This function should return one tuple (LinearRegression_R2_test_score, Lasso_R2_test_score)
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Lasso, LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.regression import r2_score # r2_score = (y_true, y_predicted)
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
def getr2fromDataPolyFit(x, y, poly_degree):
    r2_test = 0
    r2_train = 0

    y_pred_train = []
    y_pred_test = []
    X_train, X_test, y_train, y_test = train_test_split(x.reshape(-1, 1), y, random_state=0)

    X_F2_poly = PolynomialFeatures(degree=poly_degree).fit_transform(x.reshape(-1, 1))
    X_train1, X_test1, y_train1, y_test1 = train_test_split(X_F2_poly, y, random_state = 0)
    linreg = LinearRegression().fit(X_train1, y_train1)
    for i in range(0,len(X_train)):
        y_val = linreg.intercept_
        for j in range(0, poly_degree):
            y_val = y_val + X_train[i]**(j+1)*linreg.coef_[j+1]
        y_pred_train.append(y_val)

    for i in range(0,len(X_test)):
        y_val = linreg.intercept_
        for j in range(0, poly_degree):
            y_val = y_val + X_test[i]**(j+1)*linreg.coef_[j+1]
        y_pred_test.append(y_val)

    r2_train = r2_score(y_train, y_pred_train)
    r2_test = r2_score(y_test, y_pred_test)
    return (r2_train, r2_test)

# def answer_four():
np.random.seed(0)
n = 15
x = np.linspace(0,10,n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10

X_train, X_test, y_train, y_test = train_test_split(x.reshape(-1, 1), y, random_state=0)

r2_test = []
r2_train = []

r2_tr, r2_te = getr2fromDataPolyFit(x,y,12)
r2_train.append(r2_tr)
r2_test.append(r2_te)

scaler = MinMaxScaler()

X_F2_poly = PolynomialFeatures(degree=12).fit_transform(x.reshape(-1, 1))
X_train1, X_test1, y_train1, y_test1 = train_test_split(X_F2_poly, y, random_state = 0)

X_train_scaled = scaler.fit_transform(X_train1)
X_test_scaled = scaler.transform(X_test1)

linlasso = Lasso(alpha=0.01, max_iter = 10000).fit(X_train_scaled, y_train1)
r2_train.append(linlasso.score(X_train_scaled, y_train1))
r2_test.append(linlasso.score(X_test_scaled, y_test1))

print(r2_train,r2_test)