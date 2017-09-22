# ### Question 5
# 
# Train a logisitic regression classifier with default parameters using X_train and y_train.
# 
# For the logisitic regression classifier, create a precision recall curve and a 
# roc curve using y_test and the probability estimates for X_test (probability it is fraud).
# 
# Looking at the precision recall curve, what is the recall when the precision is `0.75`?
# 
# Looking at the roc curve, what is the true positive rate when the false positive rate is `0.16`?
# 
# *This function should return a tuple with two floats, i.e. `(recall, true positive rate)`.*

# X_train, X_test, y_train, y_test = train_test_split(X, y_binary_imbalanced, random_state=0)

# y_score_lr = lr.fit(X_train, y_train).decision_function(X_test)
# fpr_lr, tpr_lr, _ = roc_curve(y_test, y_score_lr)
# roc_auc_lr = auc(fpr_lr, tpr_lr)
import numpy as np
import pandas as pd
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split

df = pd.read_csv('fraud_data.csv')

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# def answer_five():
        
#     # Your code here
    
#     return # Return your answer
