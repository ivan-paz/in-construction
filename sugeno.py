# -*- coding: utf-8 -*-
"""
Script for perform k-cross-validation of a fuzzy-classifier
in which the output is calculated in the following way:

1. For a new unseen instance each rule produces a firing strenght
2. Each class is codify into a number 1, 2, 3 . . . 
3. Each of the t is multiply by the class of the rule
   t1 * 1 + t2 * 2 + t3 * 3
   The sum is normalized by the sum of the t's
"""
#   Import functions
from cross_validation_functions import *

#   Load data
data = load_data('blip_data.csv')

#   Create k-folds for cross validation
#X,y = xy_arrays(data)
#create_train_test(X,y,10)

#   Import the scaled rules, X_test and y_test for the classifier
scaled_rules = import_scaled_rules('p_a_r_1_1.csv', 'p_a_r_2_1.csv')
X_test = X_test('X_test_1.csv')
y_test = y_test('y_test_1.csv')
scaled_test = scaled_test(X_test, data)





#-----------------------------------------------------------------------
#      Let us Suppose:

scaled_rules =[
[ [0.0028118096003213, 0.0088371158867242], [0.021341463414634], 1.0],
[ [0.026913034745933,  0.039967865033139 ], [0.88821138211382 ], 2.0],
 [[0.33219521992368],  [0.0040650406504065, 0.40345528455285],   3.0]]

scaled_test = [
 [0.0038160273147218315, 0.009146341463414634],
 [0.0038160273147218315, 0.022357723577235773],
 [0.004820245029122314,  0.9522357723577236],
 [0.017875075316328582,  0.5853658536585366]]
 
y_test = [1.0, 1.0, 1.0, 2.0]

#------------------------------------------------------------------------
def compute_out(minimus,classes):
    sum_wz = 0
    for i in range(len(minimus)):
        print('min',minimus[i],'class',classes[i],'mult',minimus[i]*classes[i])
        sum_wz = sum_wz + (minimus[i] * classes[i])
    print(sum_wz, sum(minimus))
    sum_wz = sum_wz/sum(minimus)
    return sum_wz
    
#w1 = 0.4, w2 = 0.2 y w3=0.1
#tendrias z = 0.4*1 + 0.2*2 + 0.1*3 = 0.4+0.4+0.3 = 1.1
#y ahora lo divides por el promedio de las w, es decir 1.1 / 0.7 = 1.57
compute_out([0.4,0.2,0.1],[1,2,3])
#compute_out(minimus,classes)
#minimus = [0, 0.1, 0,  0.2, 0.1]
#classes = [1, 3,   1,  3,   2]

#-------------------------------------------------------------
#                  Re - write the Classifier
##------------------------------------------------------------
def classify(instance, rules, gamma):
    minimums = []
    classes = []
    for rule in rules:
        print('rule   :  ', rule)
        memberships = []
        vkj_wkj_values = rule_vkj_wkj(rule)
        print('vkj_wkj: ', vkj_wkj_values)
        for i in range(len(instance)):
            xj = instance[i]
            vkj = vkj_wkj_values[i][0]
            wkj = vkj_wkj_values[i][1]
            membership=membership_kj(xj,vkj,wkj,gamma)
            memberships.append(membership)
        print('memberships: ', memberships)
        minimum = min(memberships)
        minimums.append(minimum)
        classes.append(rule[-1])
        #print(minimum,'class', rule[-1])
    aggregation = compute_out(minimums,classes)
    classification = [abs(aggregation-1),abs(aggregation-2),abs(aggregation-3)]
    print('classification', classification, aggregation)
    classification = [abs(aggregation - 1),abs(aggregation - 2),abs(aggregation - 3)].index(min(classification))+1
    return classification
    #maximum=max(minimums)
    #index = minimums.index(maximum)
    #classification = rules[index][-1]
    #return classification        
    
#    e.g of classify
#Example
classify( [0.0028118096003213, 0.021341463414634],scaled_rules, 1) #Class 1

scaled_rules =[
[ [0.0028118096003213, 0.0088371158867242], [0.021341463414634], 1.0],
[ [0.026913034745933,  0.039967865033139 ], [0.88821138211382 ], 2.0],
 [[0.33219521992368],  [0.0040650406504065,   0.40345528455285],   3.0]]
 
 inst = [0.0028118096003213,0.021341463414634]
 


classify( [0.026913034745933,0.88821138211382  ],scaled_rules, 0.1) #Class 2
classify( [0.33219521992368, 0.0040650406504065],scaled_rules, 0.1) #Class 3

#------------------------------------------------------






#Manual
y_pred = []
for instance in scaled_test:
    print('instance',instance)
    classification = classify(instance,scaled_rules, 0.5) 
    print('classification',classification)   
    y_pred.append(classification)
accuracy_score(y_test, y_pred)


count = 0
for i in range(len(scaled_test)):
    instance = scaled_test[i] 
    print('--------------------------------------------------')
    classification = classify(instance, scaled_rules, 0.1)
    print('classification :', classification)
    if classification == y_test[i]:
        count = count + 1
        print('classified correctly!!! ')
    else:
        print('check this')
print('score: ',count) #/ len(scaled_test))








