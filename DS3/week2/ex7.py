# ### Question 7
# 
# Based on the scores from question 6, what gamma value corresponds to a model 
# that is underfitting (and has the worst test set accuracy)? What gamma value 
# corresponds to a model that is overfitting (and has the worst test set accuracy)? 
# What choice of gamma would be the best choice for a model with good generalization 
# performance on this dataset (high accuracy on both training and test set)? 
# Note: there may be multiple correct solutions to this question.
# 
# (Hint: Try plotting the scores from question 6 to visualize the relationship 
# between gamma and accuracy.)
# 
# *This function should return one tuple with the degree values in this order: 
# `(Underfitting, Overfitting, Good_Generalization)`*

# def answer_seven():
    
train = [ 0.56647847,  0.93155951,  0.99039881,  1.,          1.,          1.,        ]
test = [ 0.56768547,  0.92959558,  0.98965952,  1.,          0.99507994,  0.52240279]
results = []
under = "Underfitting"
over = "Overfitting"
good = "Good_Generalization"

for i in range(0, len(train)):
    fit = ""
    if train[i] > 0.70 :
        if test[i] > 0.70 :
            fit = good
        else :
            fit = over
    else :
        fit = under
    results.append(fit)


print(results)
# return (0.0001,10,0.1)
    # Your code here
    
    # return # Return your answer

