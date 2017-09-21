# ### Question 2
# 
# Using `X_train`, `X_test`, `y_train`, and `y_test` (as defined above), 
# train a dummy classifier that classifies everything as the majority class of the training 
# data. What is the accuracy of this classifier? What is the recall?
# 
# *This function should a return a tuple with two floats, i.e. `(accuracy score, recall score)`.*


# Use X_train, X_test, y_train, y_test for all of the following questions
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd

df = pd.read_csv('fraud_data.csv')

X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Negative class (0) is most frequent
dummy_majority = DummyClassifier(strategy = 'most_frequent').fit(X_train, y_train)
# Therefore the dummy 'most_frequent' classifier always predicts class 0
y_majority_predicted = dummy_majority.predict(X_test)
recall = recall_score(y_test, y_majority_predicted)
accuracy = accuracy_score(y_test, y_majority_predicted)

print(recall) # (true pos)/(true pos + false neg)
print(accuracy) #(true pos + true neg)/total
# def answer_two():
    
    
    # Your code here
    
    # return # Return your answer
