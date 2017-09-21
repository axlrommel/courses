# Based on the  R2R2  scores from question 2 (degree levels 0 through 9), what degree level corresponds to a 
# model that is underfitting? What degree level corresponds to a model that is overfitting? What choice of 
# degree level would provide a model with good generalization performance on this dataset? Note: there may be
#  multiple correct solutions to this question.
# (Hint: Try plotting the  R2R2  scores from question 2 to visualize the relationship between degree level and  R2R2 )
# This function should return one tuple with the degree values in this order: (Underfitting, Overfitting, Good_Generalization)

# def answer_three():
    
train = [0.0, 0.42924577812346643, 0.45109980444082465, 0.58719953687798498, 0.91941944717693125, 
    0.97578641430682078, 0.99018233247950893, 0.99352509278404955, 0.99637545387737891, 0.99803706256506819]
test = [-0.47808641737141788, -0.45237104233936654, -0.068569841499159345, 0.00533105294577918, 0.73004942818688834, 
    0.87708300916241511, 0.92140939815372302, 0.92021504108958052, 0.63247947213904609, -0.64524869871765911]
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

    # return # Return your answer

