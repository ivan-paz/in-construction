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
from cross_validation_functions import *

#   Load data
data = load_data('blip_data.csv')

#   Create k-folds for cross validation
X,y = xy_arrays(data)
create_train_test(X,y,10)


##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                 Run SuperCollider file
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

accuracy = []
file_number = -1
for i in range(10):
    file_number += 1
    print(file_number)
#   Import functions
    from cross_validation_functions import *
    scaled_rules = import_scaled_rules('p_a_r_1_'+str(file_number)+'.csv','p_a_r_2_'+str(file_number)+'.csv')
    X_test = X_test('X_test_'+str(file_number)+'.csv')
    y_test = y_test('y_test_'+str(file_number)+'.csv')
    scaled_test = scaled_test(X_test,data)
    accuracy.append(get_accuracy_score(scaled_test,y_test,scaled_rules, 2))

from statistics import mean
mean(accuracy)


"""
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                    Manual version
             selecting individual partitions
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
"""
#   Import functions
from cross_validation_functions import *
#Import the scaled rules, X_test and y_test for the classifier
scaled_rules = import_scaled_rules('p_a_r_1_1.csv', 'p_a_r_2_1.csv')
X_test = X_test('X_test_1.csv')
y_test = y_test('y_test_1.csv')
scaled_test = scaled_test(X_test,data)
get_accuracy_score(scaled_test,y_test,scaled_rules, 20)


#.................................................................
count = 0
for i in range(len(scaled_test)):
    instance = scaled_test[i]
    classification = classify(instance, scaled_rules, 4)
    print('classification :', classification)
    if classification == y_test[i]:
        count = count + 1
    else:
        print('check this')
print( count / len(scaled_test))


