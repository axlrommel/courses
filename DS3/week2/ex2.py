# Write a function that fits a polynomial LinearRegression model on the training data X_train 
# for degrees 0 through 9. For each model compute the  R2R2 (coefficient of determination) 
# regression score on the training data as well as the the test data, and return both of these arrays in a tuple.
# This function should return one tuple of numpy arrays (r2_train, r2_test). Both arrays should have shape (10,)

def answer_two():
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.metrics.regression import r2_score

    # Your code here

    return # Your answer here

