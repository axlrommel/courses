import numpy as np
import pandas as pd


# ### Question 1
# Import the data from `fraud_data.csv`. 
# What percentage of the observations in the dataset are instances of fraud?
# 
# *This function should return a float between 0 and 1.* 

# def answer_one():
    
df = pd.read_csv('fraud_data.csv')
temp = df.groupby('Class').count()
vals = dict(temp['Amount'])

#0 is not fraud, and 1 is fraud
print(vals[1]/(vals[0] + vals[1]))    
    # Your code here
    
    # return # Return your answer