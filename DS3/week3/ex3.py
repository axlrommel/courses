# ### Question 3
# 
# Using X_train, X_test, y_train, y_test (as defined above), 
# train a SVC classifer using the default parameters. What is the accuracy, recall, 
# and precision of this classifier?
# 
# *This function should a return a tuple with three floats, 
# i.e. `(accuracy score, recall score, precision score)`.*

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd

df = pd.read_csv('fraud_data.csv')

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

svc_fit = SVC().fit(X_train, y_train)
y_predicted = svc_fit.predict(X_test)
recall = recall_score(y_test, y_predicted)
accuracy = accuracy_score(y_test, y_predicted)
precision = precision_score(y_test, y_predicted)

print(accuracy) #(true pos + true neg)/total
print(recall) # (true pos)/(true pos + false neg)
print(precision)