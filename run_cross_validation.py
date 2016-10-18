#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Created on Fri Oct 14 17:56:23 2016
@author: ivan

File for automatically run k-fold cross-validation

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
#   Import functions
from automated_k_cross_validation import *


#   Load data
data = load_data('blip_data.csv')

#   Create k-folds for cross validation
#X,y = xy_arrays(data)
#create_train_test(X,y,10)

#   Import the scaled rules, X_test and y_test for the classifier
scaled_rules = import_scaled_rules('p_a_r_1_1.csv', 'p_a_r_2_1.csv')
X_test = X_test('X_test_1.csv')
y_test = y_test('y_test_1.csv')
scaled_test = scaled_test(X_test,data)

get_accuracy_score(scaled_test,y_test, 4)





#Manual
y_pred = []
for instance in scaled_test:
    print(instance)
    classification = classify(instance,scaled_rules, 4)
    print(classification)
    y_pred.append(classification)
accuracy_score(y_test, y_pred)








count = 0
for i in range(len(scaled_test)):
    instance = scaled_test[i]
    classification = classify(instance, scaled_rules, 4)
    print('classification :', classification)
    if classification == y_test[i]:
        count = count + 1
    else:
        print('check this')
print(count/len(scaled_test))



0    1   2   3   4   5   6   7   8   9
16   19  16  17  13  15 15  13   13  16
21   21  21  21  21  21 20  20   20  20


(16/21)+   (19/21)+  (16/21) +( 17/21) +( 13/21)  +(15/21) +(15/20)  +(13/20)  +( 13/20) +( 16/20)


(17/21)+(18/21)+(15/21)+(17/21)+(15/21)+(13/21)+(17/20)+(16/20)+(15/20)+(16/20)




(19/21)+(20/21)+(21/21)+(17/21)+(19/21)+(19/21)+(19/20)+(17/20)+(15/20)+(16/20)


