#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
====================================================================
             Automatic plotting of membership functions
====================================================================
"""
#Import
import csv
import matplotlib.pyplot as plt


#===================================================================
#                            functions
#===================================================================

def countClasses(rules):
    classes = []
    for rule in rules:
        if rule[-1] not in classes:
            classes.append(rule[-1])
    return classes

def separateRules(rules):
    classes = countClasses(rules)
    rules_by_class = [ [ ] for x in range(len(classes))]
    for rule in rules:
        index = int(rule[-1]-1)
        rules_by_class[index].append(rule)
    return rules_by_class


# x resolution
def xrange(steps):
    xarray = []
    step = 1/steps
    number = 0 - step
    for i in range(0,steps +1):
        number = number + step
        xarray.append(number)
    return xarray

#............................
#  membership function
#  trapezoidal
#............................    
def membership_kj(xj,vkj,wkj,gamma):
    membership = 1/2 *(max(0,1-max(0,gamma*min(1,xj-wkj))) + max(0,1-max(0,gamma*min(1,vkj-xj))))
    return membership
#...........................


def plotRules(rules,x_range, gamma, line_color):
    for rule in rules:
        vkj = rule[0]
        wkj = rule[-2]
       #print([vkj,wkj])
        function = membershipValues(x_range,vkj,wkj,gamma)
        plt.plot(x_range,function, color= line_color)
    plt.show()


def membershipValues(x_range,vkj,wkj,gamma):
    membershipValues = []
    for i in x_range:
        membership_value = membership_kj(i,vkj,wkj,gamma)
        #print(membership_value)
        membershipValues.append(membership_value)
    return membershipValues

##.....................................
#       PLOTTING RULES
##.....................................


##      first parameter
##.....................................
#  import data
data = []
#ifile  = open('prueba.csv', "r", encoding="utf8")
ifile  = open('p_a_r_1.csv', "r", encoding="utf8")
read = csv.reader(ifile)
for row in read :
    temporal_row = []
    #print(row)
    for a in row:
        b = float(a)
        temporal_row.append(b)
    data.append(temporal_row)

##...........................................
x_range = xrange(100)
rules_by_class = separateRules(data)
plotRules(rules_by_class[0],x_range,10,'r')
plotRules(rules_by_class[1],x_range,10,'b')
plotRules(rules_by_class[2],x_range,10,'y')


##-----------------------------------------------------------
##    second parameter

#  import data
data = []
ifile  = open('p_a_r_2.csv', "r", encoding="utf8")
read = csv.reader(ifile)
for row in read :
    temporal_row = []
    #print(row)
    for a in row:
        b = float(a)
        temporal_row.append(b)
    data.append(temporal_row)

x_range = xrange(100)
rules_by_class = separateRules(data)
plotRules(rules_by_class[0],x_range,10,'r')
plotRules(rules_by_class[1],x_range,10,'b')
plotRules(rules_by_class[2],x_range,10,'y')



