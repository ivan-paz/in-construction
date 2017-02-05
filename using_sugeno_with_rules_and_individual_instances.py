# -*- coding: utf-8 -*-
"""




"""

# We have a set of rules scaled into [0,1]

rules = [
[   [0.7,0.9], [0.45,0.75], 1   ],
[   [0.6,0.8], [0.8,  0.9], 2   ]
]

# And we want to classify the instance

x = [0.1, 0.1]

# Which is not contained in any of the rules

classify_sugeno(x,rules, 0.01, 2)

#-------------------------------------------------------------
#                     the Classifier
##------------------------------------------------------------
def classify_sugeno(instance, rules, gamma, classes):
    min_by_classes  = [ [], [] ] # Check this IS THE NUMBER OF CLASSES !!!!!!!!!
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
    print('aggregation is : ',aggregation)
    classification = [abs(aggregation - 1),abs(aggregation - 2),abs(aggregation - 3)]
    #print('classification',classification)
    classification = [abs(aggregation - 1),abs(aggregation - 2),abs(aggregation - 3)].index(min(classification)) + 1 
    return classification
    
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