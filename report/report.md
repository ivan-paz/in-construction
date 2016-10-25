<!---
                Documentation of the classifier
                       for its analysis 
-->
# Classifier Documentation

#Data
The data used is:

|obs  |freq |nharm|class| 
|-----|-----|-----|---| 
| 1   | 0.2 | 152 | 1 | 
| 2   | 0.2 | 189 | 1 | 
| 3   | 0.2 | 425 | 1 | 
| 4   | 0.2 | 858 | 1 | 
| 5   | 0.3 | 253 | 1 | 
| 6   | 0.4 | 136 | 1 | 
| 7   | 0.5 | 18  | 1 | 
| 8   | 0.5 | 205 | 1 | 
| 9   | 0.7 | 618 | 1 | 
| 10  | 0.9 | 433 | 1 | 
| 11  | 1   | 41  | 1 | 
| 12  | 1   | 77  | 1 | 
| 13  | 1   | 526 | 1 | 
| 14  | 1   | 949 | 1 | 
| 15  | 2   | 224 | 1 | 
| 16  | 2   | 519 | 1 | 
| 17  | 2   | 813 | 1 | 
| 18  | 2   | 984 | 1 | 
| 19  | 3   | 21  | 1 | 
| 20  | 3   | 33  | 1 | 
| 21  | 3   | 659 | 1 | 
| 22  | 4   | 9   | 1 | 
| 23  | 4   | 19  | 1 | 
| 24  | 4   | 22  | 1 | 
| 25  | 4   | 25  | 1 | 
| 26  | 4   | 26  | 1 | 
| 27  | 4   | 349 | 1 | 
| 28  | 4   | 609 | 1 | 
| 29  | 5   | 14  | 1 | 
| 30  | 5   | 361 | 1 | 
| 31  | 5   | 937 | 1 | 
| 32  | 6   | 7   | 1 | 
| 33  | 6   | 8   | 1 | 
| 34  | 6   | 24  | 1 | 
| 35  | 7   | 12  | 1 | 
| 36  | 7   | 27  | 1 | 
| 37  | 8   | 16  | 1 | 
| 38  | 8   | 48  | 1 | 
| 39  | 8   | 783 | 1 | 
| 40  | 9   | 21  | 1 | 
| 41  | 9   | 342 | 1 | 
| 42  | 9   | 417 | 1 | 
| 43  | 10  | 1   | 1 | 
| 44  | 10  | 16  | 1 | 
| 45  | 10  | 20  | 1 | 
| 46  | 10  | 28  | 1 | 
| 47  | 10  | 88  | 1 | 
| 48  | 11  | 11  | 1 | 
| 49  | 11  | 121 | 1 | 
| 50  | 11  | 274 | 1 | 
| 51  | 12  | 5   | 2 | 
| 52  | 14  | 10  | 1 | 
| 53  | 14  | 13  | 1 | 
| 54  | 14  | 418 | 1 | 
| 55  | 14  | 930 | 1 | 
| 56  | 15  | 5   | 2 | 
| 57  | 15  | 22  | 2 | 
| 58  | 15  | 23  | 1 | 
| 59  | 15  | 58  | 1 | 
| 60  | 16  | 99  | 1 | 
| 61  | 17  | 751 | 2 | 
| 62  | 18  | 5   | 1 | 
| 63  | 18  | 28  | 1 | 
| 64  | 18  | 242 | 1 | 
| 65  | 18  | 576 | 2 | 
| 66  | 19  | 10  | 2 | 
| 67  | 19  | 13  | 2 | 
| 68  | 19  | 275 | 2 | 
| 69  | 19  | 740 | 2 | 
| 70  | 20  | 6   | 2 | 
| 71  | 22  | 9   | 2 | 
| 72  | 23  | 7   | 2 | 
| 73  | 23  | 700 | 2 | 
| 74  | 23  | 803 | 2 | 
| 75  | 27  | 9   | 2 | 
| 76  | 27  | 829 | 2 | 
| 77  | 27  | 874 | 2 | 
| 78  | 28  | 2   | 3 | 
| 79  | 28  | 42  | 2 | 
| 80  | 29  | 451 | 2 | 
| 81  | 30  | 796 | 2 | 
| 82  | 31  | 445 | 2 | 
| 83  | 31  | 610 | 2 | 
| 84  | 32  | 220 | 2 | 
| 85  | 32  | 221 | 2 | 
| 86  | 32  | 289 | 2 | 
| 87  | 34  | 471 | 2 | 
| 88  | 35  | 7   | 2 | 
| 89  | 35  | 674 | 2 | 
| 90  | 36  | 229 | 2 | 
| 91  | 37  | 8   | 2 | 
| 92  | 37  | 27  | 2 | 
| 93  | 37  | 600 | 2 | 
| 94  | 38  | 3   | 2 | 
| 95  | 38  | 394 | 2 | 
| 96  | 38  | 665 | 2 | 
| 97  | 39  | 37  | 2 | 
| 98  | 40  | 874 | 2 | 
| 99  | 41  | 33  | 2 | 
| 100 | 41  | 646 | 2 | 
| 101 | 42  | 3   | 3 | 
| 102 | 42  | 7   | 2 | 
| 103 | 42  | 101 | 2 | 
| 104 | 42  | 149 | 2 | 
| 105 | 42  | 506 | 2 | 
| 106 | 43  | 17  | 2 | 
| 107 | 43  | 455 | 2 | 
| 108 | 44  | 11  | 2 | 
| 109 | 46  | 133 | 2 | 
| 110 | 47  | 335 | 2 | 
| 111 | 47  | 838 | 2 | 
| 112 | 48  | 664 | 2 | 
| 113 | 50  | 15  | 2 | 
| 114 | 50  | 34  | 2 | 
| 115 | 53  | 61  | 2 | 
| 116 | 55  | 10  | 2 | 
| 117 | 56  | 5   | 2 | 
| 118 | 56  | 16  | 2 | 
| 119 | 57  | 38  | 2 | 
| 120 | 57  | 838 | 2 | 
| 121 | 58  | 42  | 2 | 
| 122 | 59  | 1   | 3 | 
| 123 | 65  | 97  | 2 | 
| 124 | 70  | 16  | 2 | 
| 125 | 70  | 35  | 2 | 
| 126 | 71  | 38  | 2 | 
| 127 | 73  | 1   | 3 | 
| 128 | 73  | 10  | 3 | 
| 129 | 73  | 14  | 2 | 
| 130 | 73  | 42  | 2 | 
| 131 | 75  | 4   | 3 | 
| 132 | 78  | 6   | 3 | 
| 133 | 80  | 1   | 3 | 
| 134 | 80  | 17  | 2 | 
| 135 | 81  | 0   | 3 | 
| 136 | 87  | 2   | 3 | 
| 137 | 87  | 13  | 2 | 
| 138 | 90  | 2   | 3 | 
| 139 | 92  | 20  | 2 | 
| 140 | 94  | 12  | 2 | 
| 141 | 95  | 31  | 2 | 
| 142 | 96  | 27  | 2 | 
| 143 | 97  | 0   | 3 | 
| 144 | 98  | 10  | 2 | 
| 145 | 98  | 49  | 2 | 
| 146 | 101 | 3   | 3 | 
| 147 | 104 | 498 | 2 | 
| 148 | 105 | 4   | 3 | 
| 149 | 108 | 233 | 2 | 
| 150 | 109 | 3   | 3 | 
| 151 | 109 | 4   | 3 | 
| 152 | 114 | 9   | 3 | 
| 153 | 116 | 1   | 3 | 
| 154 | 118 | 67  | 2 | 
| 155 | 120 | 47  | 2 | 
| 156 | 127 | 113 | 2 | 
| 157 | 128 | 15  | 3 | 
| 158 | 131 | 368 | 2 | 
| 159 | 133 | 8   | 3 | 
| 160 | 136 | 7   | 3 | 
| 161 | 138 | 487 | 2 | 
| 162 | 145 | 8   | 3 | 
| 163 | 145 | 361 | 2 | 
| 164 | 151 | 356 | 2 | 
| 165 | 156 | 595 | 2 | 
| 166 | 158 | 817 | 2 | 
| 167 | 165 | 687 | 2 | 
| 168 | 168 | 376 | 2 | 
| 169 | 170 | 486 | 2 | 
| 170 | 201 | 834 | 2 | 
| 171 | 202 | 483 | 2 | 
| 172 | 223 | 229 | 2 | 
| 173 | 229 | 607 | 2 | 
| 174 | 255 | 653 | 3 | 
| 175 | 315 | 359 | 3 | 
| 176 | 331 | 4   | 3 | 
| 177 | 331 | 397 | 3 | 
| 178 | 333 | 513 | 3 | 
| 179 | 335 | 17  | 3 | 
| 180 | 377 | 5   | 3 | 
| 181 | 391 | 435 | 3 | 
| 182 | 393 | 173 | 3 | 
| 183 | 446 | 834 | 3 | 
| 184 | 453 | 118 | 3 | 
| 185 | 464 | 4   | 3 | 
| 186 | 471 | 280 | 3 | 
| 187 | 480 | 868 | 3 | 
| 188 | 482 | 31  | 3 | 
| 189 | 493 | 676 | 3 | 
| 190 | 531 | 890 | 3 | 
| 191 | 582 | 4   | 3 | 
| 192 | 586 | 4   | 3 | 
| 193 | 597 | 506 | 3 | 
| 194 | 614 | 3   | 3 | 
| 195 | 614 | 947 | 3 | 
| 196 | 637 | 17  | 3 | 
| 197 | 672 | 2   | 3 | 
| 198 | 751 | 99  | 3 | 
| 199 | 761 | 2   | 3 | 
| 200 | 792 | 766 | 3 | 
| 201 | 806 | 3   | 3 | 
| 202 | 854 | 811 | 3 | 
| 203 | 900 | 8   | 3 | 
| 204 | 944 | 10  | 3 | 
| 205 | 980 | 6   | 3 | 
| 206 | 996 | 755 | 3 | 

The data is splited for 10-Folds cross-validation using scikit K-Folds cross-validator. The accuracy is calculated by using the sklearn.metrics accuracy\_score.

## Parameters
The parameters used are the following.
For the rule extraction algorithm:
frequency: from 0 to inf threshold = 1000
number of upper harmonics: form 0 to inf threshold = 1000

For the classifier:
gamma = 2

## Results
The individual accuracies are:
 
[ 1.0, 1.0, 1.0, 0.952, 0.904, 1.0, 0.949, 0.900, 0.900, 0.949 ]

And the accuracy of 10-fold cross-validation is: 0.955

## Analysis
### Rules
Rules extracted by the rule extraction function on the first training set.

|Obtained rules                                                     | 
|-------------------------------------------------------------------| 
| 0     [ [ 8     10 ]    16     1 ]                                | 
| 1     [ [ 10     18 ]    28     1 ]                               | 
| 2     [ [ 15     56 ]    5     2 ]                                | 
| 3     [ [ 19     55 ]    10     2 ]                               | 
| 4     [ [ 23     35 ]    7     2 ]                                | 
| 5     [ [ 27     40 ]    874     2 ]                              | 
| 6     [ [ 28    87    90     672 ]    2     3 ]                   | 
| 7     [ [ 28     58 ]    42     2 ]                               | 
| 8     [ [ 36     223 ]    229     2 ]                             | 
| 9     [ [ 42    101    109     614 ]    3     3 ]                 | 
| 10     [ [ 56     70 ]    16     2 ]                              | 
| 11     [ [ 59    73    80     116 ]    1     3 ]                  | 
| 12     [ [ 73     944 ]    10     3 ]                             | 
| 13     [ [ 75    109    331    464    582     586 ]    4     3 ]  | 
| 14     [ [ 81     97 ]    0     3 ]                               | 
| 15     [ [ 133     145 ]    8     3 ]                             | 
| 16     [ [ 335     637 ]    17     3 ]                            | 
| 17     [ 0.2     [ 152    189    425     858 ]     1 ]            | 
| 18     [ 0.5     [ 18     205 ]     1 ]                           | 
| 19     [ 1     [ 41    77    526     949 ]     1 ]                | 
| 20     [ 2     [ 519     813 ]     1 ]                            | 
| 21     [ 3     [ 21     33 ]     1 ]                              | 
| 22     [ 4     [ 9    19    22    25    26     349 ]     1 ]      | 
| 23     [ 5     [ 14     937 ]     1 ]                             | 
| 24     [ 6     [ 8     24 ]     1 ]                               | 
| 25     [ 8     [ 48     783 ]     1 ]                             | 
| 26     [ 9     [ 342     417 ]     1 ]                            | 
| 27     [ 10     [ 20     88 ]     1 ]                             | 
| 28     [ 11     [ 11     121 ]     1 ]                            | 
| 29     [ 14     [ 10    13    418     930 ]     1 ]               | 
| 30     [ 15     [ 23     58 ]     1 ]                             | 
| 31     [ 19     [ 13     275 ]     2 ]                            | 
| 32     [ 23     [ 700     803 ]     2 ]                           | 
| 33     [ 31     [ 445     610 ]     2 ]                           | 
| 34     [ 32     [ 220     221 ]     2 ]                           | 
| 35     [ 37     [ 8     27 ]     2 ]                              | 
| 36     [ 38     [ 3     394 ]     2 ]                             | 
| 37     [ 41     [ 33     646 ]     2 ]                            | 
| 38     [ 42     [ 7    101    149     506 ]     2 ]               | 
| 39     [ 43     [ 17     455 ]     2 ]                            | 
| 40     [ 50     [ 15     34 ]     2 ]                             | 
| 41     [ 73     [ 14     42 ]     2 ]                             | 
| 42     [ 98     [ 10     49 ]     2 ]                             | 
| 43     [ 8     [ 16     48 ]     1 ]                              | 
| 44     [ 10     [ 16    20    28     88 ]     1 ]                 | 
| 45     [ 15     [ 5     22 ]     2 ]                              | 
| 46     [ 18     [ 28     242 ]     1 ]                            | 
| 47     [ 19     [ 10    13    275     740 ]     2 ]               | 
| 48     [ 23     [ 7     700 ]     2 ]                             | 
| 49     [ 27     [ 829     874 ]     2 ]                           | 
| 50     [ 35     [ 7     674 ]     2 ]                             | 
| 51     [ 56     [ 5     16 ]     2 ]                              | 
| 52     [ 70     [ 16     35 ]     2 ]                             | 
| 53     [ 73     [ 1     10 ]     3 ]                              | 
| 54     [ 109     [ 3     4 ]     3 ]                              | 
| 55     [ 331     [ 4     397 ]     3 ]                            | 
| 56     [ 614     [ 3     947 ]     3 ]                            | 
| 57     [ [ 42     101 ]    3     3 ]                              | 
| 58     [ [ 59     80 ]    1     3 ]                               | 
| 59     [ [ 75    464    582     586 ]    4     3 ]                | 


Some of the rules can stil be compressed (but not much).
For example rules 27, 44, 46, and 1 came from different permutations of the data during the compression.


### Membership functions

The trapezoidal membership functions for each parameter are given by the equation:

membership\_kj(xj,vkj,wkj,gamma):
membership = 1/2 * (max(0,1-max(0,gamma * min(1,xj-wkj))) + max(0,1-max(0,gamma * min(1,vkj-xj))))

Where xj is the jth value of any input instance. vkj and wkj are the minimum and maximum values for the jth parameter of rule k. These values are the min amd max of the interval [vkj,. . . , wkj] if the rule has an interval in the jth parameter or vkj = wkj = value, if the rule has a value at the jth parameter. And gamma is the parameter that control the spread of the "rim" of the trapezoidal functions.

#### Membership functions plots
Plots for the membership functions of the parameters 1 and 2, for classes rhythmic, rough and tone, are display below.


![title](path/to/your/image)
![]