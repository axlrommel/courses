# ### Question 6
# 
# For this question, we're going to use the `validation_curve` function in `sklearn.model_selection` 
# to determine training and test scores for a Support Vector Classifier (`SVC`) 
# with varying parameter values.  Recall that the validation_curve function, 
# in addition to taking an initialized unfitted classifier object, 
# takes a dataset as input and does its own internal train-test splits to compute results.
# 
# Because creating a validation curve requires fitting multiple models, for performance 
# reasons this question will use just a subset of the original mushroom dataset: please use 
# the variables X_subset and y_subset as input to the validation curve function 
# (instead of X_mush and y_mush) to reduce computation time.
# 
# The initialized unfitted classifier object we'll be using is a Support Vector Classifier 
# with radial basis kernel.  So your first step is to create an `SVC` object with default 
# parameters (i.e. `kernel='rbf', C=1`) and `random_state=0`. Recall that the kernel width 
# of the RBF kernel is controlled using the `gamma` parameter.  
# 
# With this classifier, and the dataset in X_subset, y_subset, explore the effect of 
# `gamma` on classifier accuracy by using the `validation_curve` function to find the 
# training and test scores for 6 values of `gamma` from `0.0001` to `10` 
# (i.e. `np.logspace(-4,1,6)`). Recall that you can specify what scoring metric you want 
# validation_curve to use by setting the "scoring" parameter.  In this case, we want 
# to use "accuracy" as the scoring metric.
# 
# For each level of `gamma`, `validation_curve` will fit 3 models on different subsets 
# of the data, returning two 6x3 (6 levels of gamma x 3 fits per level) arrays of the 
# scores for the training and test sets.
# 
# Find the mean score across the three models for each level of `gamma` for both arrays, 
# creating two arrays of length 6, and return a tuple with the two arrays.
# 
# e.g.
# 
# if one of your array of scores is
# 
#     array([[ 0.5,  0.4,  0.6],
#            [ 0.7,  0.8,  0.7],
#            [ 0.9,  0.8,  0.8],
#            [ 0.8,  0.7,  0.8],
#            [ 0.7,  0.6,  0.6],
#            [ 0.4,  0.6,  0.5]])
#        
# it should then become
# 
#     array([ 0.5,  0.73333333,  0.83333333,  0.76666667,  0.63333333, 0.5])
# 
# *This function should return one tuple of numpy arrays `(training_scores, test_scores)` 
# where each array in the tuple has shape `(6,)`.*

# def answer_six():
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve
from sklearn.model_selection import train_test_split


mush_df = pd.read_csv('mushrooms.csv')
mush_df2 = pd.get_dummies(mush_df)

X_mush = mush_df2.iloc[:,2:]
y_mush = mush_df2.iloc[:,1]

# use the variables X_train2, y_train2 for Question 5
X_train2, X_test2, y_train2, y_test2 = train_test_split(X_mush, y_mush, random_state=0)

# For performance reasons in Questions 6 and 7, we will create a smaller version of the
# entire mushroom dataset for use in those questions.  For simplicity we'll just re-use
# the 25% test split created above as the representative subset.
#
# Use the variables X_subset, y_subset for Questions 6 and 7.
X_subset = X_test2
y_subset = y_test2

param_range = np.logspace(-4, 1, 6)
print(param_range)
train_scores,test_scores = validation_curve(SVC(),X_subset,y_subset, param_name="gamma", 
    param_range = param_range, scoring='accuracy')

train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

print(train_scores_mean)
print(test_scores_mean)

plt.title("Validation Curve with SVM")
plt.xlabel("$\gamma$")
plt.ylabel("Score")
plt.ylim(0.0, 1.1)
lw = 2
plt.semilogx(param_range, train_scores_mean, label="Training score",
             color="darkorange", lw=lw)
plt.fill_between(param_range, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, alpha=0.2,
                 color="darkorange", lw=lw)
plt.semilogx(param_range, test_scores_mean, label="Cross-validation score",
             color="navy", lw=lw)
plt.fill_between(param_range, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, alpha=0.2,
                 color="navy", lw=lw)
plt.legend(loc="best")
plt.show()


    # Your code here

    # return # Your answer here
