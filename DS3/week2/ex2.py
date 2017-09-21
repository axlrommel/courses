# Write a function that fits a polynomial LinearRegression model on the training data X_train 
# for degrees 0 through 9. For each model compute the  R2R2 (coefficient of determination) 
# regression score on the training data as well as the the test data, and return both of these arrays in a tuple.
# This function should return one tuple of numpy arrays (r2_train, r2_test). Both arrays should have shape (10,)

#def answer_two():
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
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



np.random.seed(0)
n = 15
x = np.linspace(0,10,n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10

X_train, X_test, y_train, y_test = train_test_split(x.reshape(-1, 1), y, random_state=0)

r2_test = []
r2_train = []

# degree 0 : use the mean
y_mean = np.mean(y_train)
y_pred_train = [y_mean] * len(y_train)
y_pred_test = [y_mean] * len(y_test)
r2_train.append(r2_score(y_train, y_pred_train))
r2_test.append(r2_score(y_test, y_pred_test))

# degree 1
linreg = LinearRegression().fit(X_train, y_train)
y_pred_train = list(map(lambda x: x * linreg.coef_[0] + linreg.intercept_,X_train ))
y_pred_test = list(map(lambda x: x * linreg.coef_[0] + linreg.intercept_,X_test ))
r2_train.append(r2_score(y_train, y_pred_train))
r2_test.append(r2_score(y_test, y_pred_test))

for i in range(2,10):
    r2_tr, r2_te = getr2fromDataPolyFit(x,y,i)
    r2_train.append(r2_tr)
    r2_test.append(r2_te)

labels = ['{0}'.format(i) for i in range(len(r2_train))]

plt.title("ex 2")
plt.plot (r2_train, r2_test, 'r-')
plt.xlabel("Train")
plt.ylabel("Test")
for label, x, y in zip(labels, r2_train[:], r2_test[:]):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-20, 20),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
plt.show()
    #return # Your answer here

