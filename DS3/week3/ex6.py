# ### Question 6
# 
# Perform a grid search over the parameters listed below for a Logisitic Regression classifier, 
# using recall for scoring and the default 3-fold cross validation.
# 
# `'penalty': ['l1', 'l2']`
# 
# `'C':[0.01, 0.1, 1, 10, 100]`
# 
# From `.cv_results_`, create an array of the mean test scores of each parameter 
# combination. i.e.
# 
# |      	| `l1` 	| `l2` 	|
# |:----:	|----	|----	|
# | **`0.01`** 	|    ?	|   ? 	|
# | **`0.1`**  	|    ?	|   ? 	|
# | **`1`**    	|    ?	|   ? 	|
# | **`10`**   	|    ?	|   ? 	|
# | **`100`**   	|    ?	|   ? 	|
# 
# <br>
# 
# *This function should return a 5 by 2 numpy array with 10 floats.* 
# 
# *Note: do not return a DataFrame, just the values denoted by '?' above in a numpy array.*
# 1. Created logistic regression object

# 2. Set the grid_values {'penalty': ['l1'], 'C':[0.01, 0.1, 1, 10, 100]}

# 3. Created a grid search object based on it with cv=3.

# 5. Fit the X_train, y_train data to the grid search object

# 6. Read results ( use .cv_results_ ) and stored it as an array

# 7. Adjusted the array shape to fit 5,2 size. ( np array method reshape )

# def answer_six():    
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
import pandas as pd

df = pd.read_csv('fraud_data.csv')

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# classifier1 = LogisticRegression(penalty='l1')
# classifier2 = LogisticRegression(penalty='l2')
classifier = LogisticRegression()
grid_values = {'C':[0.01, 0.1, 1, 10, 100], 'penalty':['l1','l2']}
clf = GridSearchCV(classifier, cv=3,param_grid=grid_values)
qq = clf.fit(X_train, y_train)
print(qq.cv_results_)
tt =qq.cv_results_['mean_test_score']
print(tt)
# clf2 = GridSearchCV(classifier2, cv=3,param_grid=grid_values)
# qq2 = clf2.fit(X_train, y_train)
# tt1 = qq2.cv_results_['mean_test_score']

qq1 = [[tt[0],tt[1]],[tt[2],tt[3]],[tt[4],tt[5]],[tt[6],tt[7]],[tt[8],tt[9]]]
# print(qq1)
    # Your code here
    
    # return # Return your answer


# Use the following function to help visualize results from the grid search
# def GridSearch_Heatmap(scores):
#     get_ipython().magic('matplotlib notebook')
#     import seaborn as sns
#     import matplotlib.pyplot as plt
#     plt.figure()
#     sns.heatmap(scores.reshape(5,2), xticklabels=['l1','l2'], yticklabels=[0.01, 0.1, 1, 10, 100])
#     plt.yticks(rotation=0);

# #GridSearch_Heatmap(answer_six())