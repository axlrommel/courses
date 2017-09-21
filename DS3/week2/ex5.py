# ### Question 5
# 
# Using `X_train2` and `y_train2` from the preceeding cell, train a DecisionTreeClassifier 
# with default parameters and random_state=0. What are the 5 most important features found by the decision tree?
# 
# As a reminder, the feature names are available in the `X_train2.columns` property, 
# and the order of the features in `X_train2.columns` matches the order of the feature importance values in the 
# classifier's `feature_importances_` property. 
# 
# *This function should return a list of length 5 containing the feature names in descending order of importance.*
# 

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


mush_df = pd.read_csv('mushrooms.csv')
mush_df2 = pd.get_dummies(mush_df)

X_mush = mush_df2.iloc[:,2:]
y_mush = mush_df2.iloc[:,1]

X_train2, X_test2, y_train2, y_test2 = train_test_split(X_mush, y_mush, random_state=0)
clf = DecisionTreeClassifier().fit(X_train2, y_train2)

importance = pd.DataFrame(data = np.transpose(clf.feature_importances_)).T
importance.columns = X_train2.columns
print(importance.T.sort_values(0, ascending = False).index.values[0:5])

