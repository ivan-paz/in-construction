# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
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
        Where max(ti) is the maximum firing strenght value for class i
        
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
"""


#-----------------------------------------------------------------
#  Trapezoidal membership function
#
def trapmf(x,a,b,c,d):
    if a == b:
        a = a + 0.00001
    if c == d:
        c = c + 0.00001
    membership = max ( min( (x-a)/(b-a), 1, (d-x)/(d-c) ), 0)
    return membership
#trapmf(0.0038160273147218315, 0, 0.0028118096003213, 0.0088371158867242, 1)
#trapmf(2,6,5,7,8)
#trapmf(0.1, 0, 0.3, 0.6, 1)
#In: trapmf(0.1, 0, 0.3, 0.6, 1)
#Out[50]: 0.33333333333333337
#trapmf(0.0038160273147218315, 0, 0.0001, 0.0001,1)
#-----------------------------------------------------------------
#.................................................................
#    calculate vkj wkj for each parameter in a rule  
def vkj_wkj(parameter):
        vkj = min(parameter)
        wkj = max(parameter)
        return vkj,wkj
#In: vkj_wkj([2,3,5,1,6,10,8])
#Out[48]: (1, 10)
def rule_vkj_wkj(rule):
    vkj_wkj_values = [ ]
    for i in range(len(rule)-1):
        vkj_wkj_values.append(vkj_wkj(rule[i]))
    return vkj_wkj_values
# In: rule_vkj_wkj([[0.0028118096003213, 0.0088371158867242], [0.021341463414634], 1.0])
#Out [   (0.0028118096003213, 0.0088371158867242),
#        (0.021341463414634, 0.021341463414634)    ]
#-----------------------------------------------------------------------
#----------------------------------------------
#  calculate_output
def calculate_output(min_by_classes):
    maximum = []
    product = 0
    for entry in min_by_classes:
        maximum.append(max(entry))
    for i in range(1, len(maximum) + 1 ):
        product = product + maximum[i - 1] * i
    return product/sum(maximum)
        
#calculate_output([[0.4285714285714315], [0.010297482837528616], [0.011487303506650524]])
#calculate_output([[0.4],[0.2],[0.1]])
#----------------------------------------------
#      Let us suppose we have the following rules scaled into [0,1]
scaled_rules =[
[ [0.0028118096003213, 0.0088371158867242], [0.021341463414634],                      1.0],
[ [0.026913034745933,  0.039967865033139 ], [0.88821138211382 ],                      2.0],
[ [0.33219521992368],                       [0.0040650406504065, 0.40345528455285],   3.0]]

#   X_test set
scaled_test = [
 [0.0038160273147218315, 0.009146341463414634],
 [0.0038160273147218315, 0.022357723577235773],
 [0.004820245029122314,  0.9522357723577236],
 [0.017875075316328582,  0.5853658536585366]]
#  Y_test_set
y_test = [1.0, 1.0, 1.0, 2.0]

# And we want to classify the instance:
x = [0.0038160273147218315, 0.009146341463414634] #Which we know is class 1
#-------------------------------------------------------------
#                  write the Classifier
##------------------------------------------------------------
def classify(instance, rules, gamma, classes):
    #minimums = [ ]
    #classes = [ ]
    min_by_classes  = [[], [], [] ] #****************
    for rule in rules:
        #print('rule   :  ', rule)
        store = int(rule[-1] - 1)
        memberships = [ ]
        vkj_wkj_values = rule_vkj_wkj(rule)
        #print('vkj_wkj: ', vkj_wkj_values)
        
        for i in range(len(instance)):
            xj = instance[i]
            vkj = vkj_wkj_values[i][0]
            wkj = vkj_wkj_values[i][1]
            #print(xj, vkj_wkj_values[i][0],vkj_wkj_values[i][1])
            if vkj == 0:
                vkj = 0.0001
            if wkj == 0:
                wkj = 0.0001
            print(xj, vkj, wkj)
            membership = trapmf( xj, 0, vkj, wkj,  0.9999)
            memberships.append(membership)
       # print(memberships)
        minimum = min(memberships)
      #  print('minimum',minimum)
        min_by_classes[store].append(minimum)
   # print(min_by_classes)
    aggregation = calculate_output(min_by_classes)
    classification = [abs(aggregation-1),abs(aggregation-2),abs(aggregation-3)]
    classification = [abs(aggregation - 1),abs(aggregation - 2),abs(aggregation - 3)].index(min(classification)) + 1 
    return classification

#    classify(x, scaled_rules, 1, 3)


#-------------------------------------------------------------------
#      Let us suppose we have the following rules and data
#-------------------------------------------------------------------
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
#            Small test
#
count = 0
for i in range(len(scaled_test)):
    instance = scaled_test[i]
    print('--------------------------------------------------')
    classification = classify(instance, scaled_rules, 0.1, 3)
    print('classification :', classification)
    if classification == y_test[i]:
        count = count + 1
        print('classified correctly!!! ')
    else:
        print('check this')
print('score: ',count / len(scaled_test))
#--------------------------------------------------------------------------


#----------------------------------------------------
#
#     Let us test the classifier with some data
#           and k times cross-validation
#----------------------------------------------------
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

#     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#-------------------------------------------------------------
#                  write the Classifier
##------------------------------------------------------------
def classify(instance, rules, gamma, classes):
    #minimums = [ ]
    #classes = [ ]
    min_by_classes  = [[], [], [] ] #****************
    for rule in rules:
        #print('rule   :  ', rule)
        store = int(rule[-1] - 1)
        memberships = [ ]
        vkj_wkj_values = rule_vkj_wkj(rule)
        #print('vkj_wkj: ', vkj_wkj_values)
        
        for i in range(len(instance)):
            xj = instance[i]
            vkj = vkj_wkj_values[i][0]
            wkj = vkj_wkj_values[i][1]
            #print(xj, vkj_wkj_values[i][0],vkj_wkj_values[i][1])
            #if vkj == 0:
             #   vkj = 0.0000001
            #if wkj == 0:
             #   wkj = 0.0000001
            #def trapmf(x,a,b,c,d): membership = max ( min( (x-a)/(b-a), 1, (d-x)/(d-c) ), 0)

            #print('b-a',vkj -(vkj - 0.01), (wkj+ 0.01)- wkj)
            
            membership = trapmf( xj, vkj - 0.01, vkj, wkj,  wkj + 0.01)
            memberships.append(membership)
       # print(memberships)
        minimum = min(memberships)
      #  print('minimum',minimum)
        min_by_classes[store].append(minimum)
   # print(min_by_classes)
    aggregation = calculate_output(min_by_classes)
    classification = [abs(aggregation-1),abs(aggregation-2),abs(aggregation-3)]
    classification = [abs(aggregation - 1),abs(aggregation - 2),abs(aggregation - 3)].index(min(classification)) + 1 
    return classification
#----------------------------------------------------
count = 0
for i in range(len(scaled_test)):
    instance = scaled_test[i] 
    print('--------------------------------------------------')
    classification = classify(instance, scaled_rules, 0.1, 3)
    print('classification :', classification)
    if classification == y_test[i]:
        count = count + 1
        print('classified correctly!!! ')
    else:
        print('check this')
    print(count)
print('score: ',count / len(scaled_test))

