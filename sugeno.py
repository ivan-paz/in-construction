# -*- coding: utf-8 -*-
"""

Functions for a rule-based fuzzy classifier

           in which the output is calculated in the following way:

    1. For a new unseen instance X = (x1, . . . xn) each rule produces a firing strengh t(xi)
       given by the minimum membership value of the xi's

    2. Each rule has an associated class codified into a number 1, 2, 3 . . . 

    3. The class if X is calculated as:
                                        max(t1) * 1 + max(t2) * 2 + max(t3) * 3
                                        ---------------------------------------
                                                   t1 + t2 + t3
                                                   
        Where max(ti) is the maximum firing strenght value for rules of class i

"""
#-----------------------------------------------------------------
#  Trapezoidal membership function
#
def trapmf(x,a,b,c,d):
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
    if sum(maximum) == 0:    # If the sum of max values == zero
        return product / 0.0000001 # Approach by  0.0000001 
    else:
        return product/sum(maximum)    
#calculate_output([[0.4285714285714315], [0.010297482837528616], [0.011487303506650524]])
#calculate_output([[0.4],[0.2],[0.1]])      
"""
#-------------------------------------------------------------
#                     the Classifier
##------------------------------------------------------------
def classify_sugeno(instance, rules, gamma, classes):
    min_by_classes  = [ [], [], [] ] # Check this !!!!!!!!!!!!!!!!!!!!!!!!!
    for rule in rules:
        store = int(rule[-1] - 1)
        memberships = [ ]
        vkj_wkj_values = rule_vkj_wkj(rule)
        for i in range(len(instance)):
            xj = instance[i]
            vkj = vkj_wkj_values[i][0]
            wkj = vkj_wkj_values[i][1]
            #print('b-a :', vkj - (vkj - 0.01), 'd -c:',  (wkj + 0.01) -  wkj)
            
            if ( vkj - vkj - 0.01 ) == 0 or ( wkj + 0.01 -  wkj) == 0 :
                membership = trapmf( xj, vkj - 0.001,  vkj,   wkj,    wkj + 0.001)
            else:
                membership = trapmf( xj, vkj - 0.01,  vkj,   wkj,    wkj + 0.01)
                
                
            memberships.append(membership)     
        minimum = min(memberships)
        min_by_classes[store].append(minimum)
    aggregation = calculate_output(min_by_classes)
    classification = [abs(aggregation-1),abs(aggregation-2),abs(aggregation-3)]
    classification = [abs(aggregation - 1),abs(aggregation - 2),abs(aggregation - 3)].index(min(classification)) + 1 
    return classification
"""
#-------------------------------------------------------------
#                     the Classifier
##------------------------------------------------------------
def classify_sugeno(instance, rules, gamma, classes):
    min_by_classes  = [ [], [], [] ] # Check this !!!!!!!!!!!!!!!!!!!!!!!!!
    for rule in rules:
        store = int( rule[-1] - 1)
        memberships = [ ]
        vkj_wkj_values = rule_vkj_wkj(rule)
        for i in range(len(instance)):
            xj = instance[i]
            vkj = vkj_wkj_values[i][0]
            wkj = vkj_wkj_values[i][1]
            #print('b-a :', vkj - (vkj - 0.01), 'd -c:',  (wkj + 0.01) -  wkj)
            
            if ( vkj - vkj - gamma ) == 0 or ( wkj + gamma -  wkj) == 0 :
                membership = trapmf( xj, vkj - (gamma/2),  vkj,   wkj,    wkj + (gamma/2))
            else:
                membership = trapmf( xj, vkj - gamma,  vkj,   wkj,    wkj + gamma)
                
                
            memberships.append(membership)     
        minimum = min(memberships)
        min_by_classes[store].append(minimum)
    aggregation = calculate_output(min_by_classes)
    classification = [abs(aggregation - 1),abs(aggregation - 2),abs(aggregation - 3)]
    classification = [abs(aggregation - 1),abs(aggregation - 2),abs(aggregation - 3)].index(min(classification)) + 1 
    return classification
"""
#----------------------------------------------
#      Let us suppose we have the following rules scaled into [0,1]
scaled_rules =[
[ [0.0028118096003213, 0.0088371158867242], [0.021341463414634],                      1.0],
[ [0.026913034745933,  0.039967865033139 ], [0.88821138211382 ],                      2.0],
[ [0.33219521992368],                       [0.0040650406504065, 0.40345528455285],   3.0]]
# And we want to classify the instance:
x = [0.0038160273147218315, 0.009146341463414634] #Which we know is class 1

# Apply the classifier to the instance
classify_sugeno(x,scaled_rules,1,3)



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
    classification = classify_sugeno(instance, scaled_rules, 0.1, 3)
    print('classification :', classification)
    if classification == y_test[i]:
        count = count + 1
        print('classified correctly!!! ')
    else:
        print('check this')
print('score: ',count / len(scaled_test))
#--------------------------------------------------------------------------
"""

#----------------------------------------------------
#
#     Let us test the classifier with some data
#           and k times cross-validation
#----------------------------------------------------
#
#           Functions for cross-validation
#
"""
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Create train and test for
k-fold-cross-validation
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
"""
import csv
import numpy as np
from sklearn.model_selection import KFold
#from sklearn.metrics import accuracy_score
np.set_printoptions(suppress=True)


def load_data(file_name):
    data = []
    with open(file_name, 'r', encoding="utf8") as file:
        read = csv.reader(file)
        for row in read:
            temporal_row = []
            for param in row:
                param = float(param)
                temporal_row.append(param)
            data.append(temporal_row)
    return data
  
#split data into X and y arrays
def xy_arrays(data):
    X=[];y=[]
    for instance in data:
        x_temp = instance[1:-1]
        X.append(x_temp)
        y_temp = instance[-1]
        y.append(y_temp)
    X = np.array(X)
    y = np.array(y)
    return X, y

# Create X_train y_train X_test and y_test

def create_train_test(X,y,n_splits):
    kf = KFold(n_splits=10, shuffle=True)
    count = -1
    for train_index, test_index in kf.split(X):
    #print("TRAIN:", train_index, "TEST:", test_index)
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        count = count + 1
        np.savetxt('X_train_'+str(count)+'.csv', X_train, fmt='%f', delimiter=',')
        np.savetxt('X_test_'+str(count)+'.csv', X_test, fmt='%f', delimiter=',')
        np.savetxt('y_train_'+str(count)+'.csv', y_train, fmt='%f', delimiter=',')
        np.savetxt('y_test_'+str(count)+'.csv', y_test, fmt='%f', delimiter=',')

#
# The files X_train and y_train are processed by rule_extraction_revision.scd
# to extract rules that are stored into p_a_r_n_nsplit.csv
#
#.................................................................
#
#          Import the values of parameter 1 and 2
#           from scaled_rules created in SuperCollider
#          -----------------------------------------------
#..................................................................
def import_scaled_rules(file, file1):
    parameter1 = []
    ifile  = open(file, "r", encoding="utf8")
    read = csv.reader(ifile)
    for row in read :
        temporal_row = []
        for a in row:
            b = float(a)
            temporal_row.append(b)
        parameter1.append(temporal_row)
    parameter2 = []
    ifile  = open(file1, "r", encoding="utf8")
    read = csv.reader(ifile)
    for row in read :
        temporal_row = []
        for a in row:
            b = float(a)
            temporal_row.append(b)
        parameter2.append(temporal_row)
    scaled_rules = []
    for i in range(len(parameter1)):
        rule = []
        par1 = parameter1[i]
        par1 = par1[0:-1]
        par2 = parameter2[i]
        par2 = par2[0:-1]
        rule.append(par1)
        rule.append(par2)
        rule.append(parameter1[i][-1])
        scaled_rules.append(rule)
    return scaled_rules    

def X_test(filename):
    X_test = []
    file = open(filename,'r', encoding="utf-8")
    read = csv.reader(file)
    for row in read:
        temporal = []
        for element in row:
            element = float(element)
            temporal.append(element)
        X_test.append(temporal)
    return X_test
        
def y_test(filename):
    y_test = []
    file = open(filename,'r', encoding="utf-8")
    read = csv.reader(file)
    for row in read:
        for element in row:
            element = float(element)
            y_test.append(element)
    return y_test
        
#Clean data    *****************   IF data do not have numbers eliminate this
def clean_data(data):
    data_without_instance_number = []
    for instance in data:
        instance = instance[1:]
        data_without_instance_number.append(instance)
    return data_without_instance_number
       
#------------------------------------------------------------------
#  find min max in data
def min_max(data):
    minmax = [[None,None]] * len(data[0])
    for instance in data:
        for idx, element in enumerate(instance):
            if minmax[idx]==[None,None]:
                minmax[idx]=[element,element]
            else:
                if element < minmax[idx][0]:
                    minmax[idx][0]=element
                if element > minmax[idx][1]:
                    minmax[idx][1]=element
    return minmax
            
#min_max(data_without_instance_number)

#  scale individual values
def scaling(instance, minimum_amd_maximum_values):
    scaled_instance = []
    for idx, parameter in enumerate(instance):
        minx = minimum_amd_maximum_values[idx][0]
        maxx = minimum_amd_maximum_values[idx][1]
        scaled = (parameter - minx) / (maxx - minx)
        scaled_instance.append(scaled)
    return scaled_instance
        
#scaled test
def scaled_test(test,data):
    scaled_test = []
    minmax = min_max(clean_data(data)) ###******IF data do not have numbers eliminate this
    for item in test:
        temporal_item = []
        #classification = item[-1]
       # item = item[:-1]
        temporal_item = (scaling(item,minmax))
        #temporal_item.append(classification)
        scaled_test.append(temporal_item)
    return scaled_test
#-----------------------------------------------------------------------------------------------------------------
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#           Run the classifier for x_test,y_test scaled into [0,1]
#                   using the rules scaled into [0,1]
#
def classify_test( x_test, y_test,rules,gamma,classes):
    count = 0
    for i in range(len(x_test)):
        instance = x_test[i]
        #print('--------------------------------------------------')
        classification = classify_sugeno(instance, rules, gamma, classes)
        #print('classification :', classification)
        if classification == y_test[i]:
            count = count + 1
            #print('classified correctly!!! ')
        #else:
            #print('check this')
        #print('partial score :', count)
    print('score: ', count / len(x_test) )
    return count/len(x_test)
