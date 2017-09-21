# ### Question 4
# 
# Using the SVC classifier with parameters `{'C': 1e9, 'gamma': 1e-07}`, 
# what is the confusion matrix when using a threshold of -220 on the decision function. 
# Use X_test and y_test.
# 
# *This function should return a confusion matrix, a 2x2 numpy array with 4 integers.*

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
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

classifier = SVC(gamma=1e-07,C=1e9)
svc_fit = classifier.fit(X_train, y_train)
y_predicted = svc_fit.predict(X_test)

print("Classification report for classifier %s:\n%s\n" %
      (classifier, metrics.classification_report(y_test, y_predicted)))
print ("Confusion matrix:\n%s" % metrics.confusion_matrix(y_test, y_predicted))

# return metrics.confusion_matrix(y_test, y_predicted)
