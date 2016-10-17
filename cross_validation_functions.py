# -*- coding: utf-8 -*-
"""
½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½

this script contains the functions for k-fold cross-validation of
a fuzzy rule-based classifier

½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½½
"""

"""
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Create train and test for
k-fold-cross-validation
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
"""
import csv
import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
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

#-----------------------------------------------------------------
#
#                         CLASSIFIER FUNCTIONS
#
#.................................................................
#  trapezoidal membership function
#.................................................................    
def membership_kj(xj,vkj,wkj,gamma):
    membership = 1/2 *(max(0,1-max(0,gamma*min(1,xj-wkj))) + max(0,1-max(0,gamma*min(1,vkj-xj))))
    return membership
#.................................................................
#    calculate vkj wkj for each parameter in a rule  
def vkj_wkj(parameter):
        vkj = min(parameter)
        wkj = max(parameter)
        return vkj,wkj

def rule_vkj_wkj(rule):
    vkj_wkj_values = []
    for i in range(len(rule)-1):
        vkj_wkj_values.append(vkj_wkj(rule[i]))
    return vkj_wkj_values
#.................................................................        
##                              classifier
##................................................................
def classify(instance, rules, gamma):
    minimums = []
    for rule in rules:
        memberships = []
        vkj_wkj_values = rule_vkj_wkj(rule)
        #print(vkj_wkj_values)
        for i in range(len(instance)):
            xj=instance[i]
            vkj=vkj_wkj_values[i][0]
            wkj=vkj_wkj_values[i][1]
            membership=membership_kj(xj,vkj,wkj,gamma)
            memberships.append(membership)
        #print(memberships)
        minimum=min(memberships)
        minimums.append(minimum)
    #print(minimums)
    maximum=max(minimums)
    index = minimums.index(maximum)
    classification = rules[index][-1]
    return classification        
    
#    e.g of classify([0.1,0.09],0.5)
#...................................................................

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


#   get accuracy
def get_accuracy_score(scaled_test,y_test,gamma):
    y_pred = []
    for instance in scaled_test:
        print(instance)
        classification = classify(instance,scaled_rules, gamma)
        print(classification)
        y_pred.append(classification)
    return accuracy_score(y_test, y_pred)
        
        
        
        
        
        
        
        
        
        
        