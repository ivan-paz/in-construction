# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------

      Script for perform k cross-validation of a rule-based fuzzy-classifier
           in which the output is calculated in the following way:

    1. For a new unseen instance X = (x1, . . . xn) each rule produces a firing strengh t(xi)
       given by the minimum membership value of the xi's

    2. Each rule has an associated class codified into a number 1, 2, 3 . . . 

    3. The class if X is calculated as:
                                        max(t1) * 1 + max(t2) * 2 + max(t3) * 3
                                        ---------------------------------------
                                                   t1 + t2 + t3
                                                   
        Where max(ti) is the maximum firing strenght value for rules of class i
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
"""

#-------------------------------------------------------------
#      Run Run Run the classification
#-------------------------------------------------------------
#   Load data
from sugeno import *
data = load_data('blip_data.csv')
#   Create k-folds for cross validation
#X,y = xy_arrays(data)
#create_train_test(X,y,10)
#   Import the scaled rules, X_test and y_test for the classifier
scaled_rules = import_scaled_rules('p_a_r_1_0.csv', 'p_a_r_2_0.csv')
X_test = X_test('X_test_0.csv')
y_test = y_test('y_test_0.csv')
scaled_test = scaled_test(X_test, data) 
classify_test( scaled_test, y_test, scaled_rules, 0.01, 3)

##--------------------- Run the classifier for the 10 folds ------------------------------
from sugeno import *
data = load_data('blip_data.csv')
accuracy = []
file_number = -1
for i in range(10):
    file_number += 1
    print(file_number)
#   Import functions
    from sugeno import *
    scaled_rules = import_scaled_rules('p_a_r_1_'+str(file_number)+'.csv','p_a_r_2_'+str(file_number)+'.csv')
    X_test = X_test('X_test_'+str(file_number)+'.csv')
    y_test = y_test('y_test_'+str(file_number)+'.csv')
    scaled_test = scaled_test(X_test,data)
    accuracy.append( classify_test( scaled_test, y_test, scaled_rules, 0.02, 3) )
from statistics import mean
mean(accuracy)

