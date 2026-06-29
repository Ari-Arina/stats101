# Last edited by Ariana, 28 June 2026
# Calculates 1-Var Stats Calculations (Measures of center and variation) --> change file name? 
#       since these values can be used to calculate other things... should I make it a class instead? rather than its own file
#       (for organization purposes, all calculations in this file should entail to 1-VAR CALC )
#   can be used to draw boxplots (must figure out how... need to learn react)
#   need to add oulier calculation (IQR, x >< Q3 or Q1 +- (1.5 * IQR)) [ -- DONE, but must check if it's correct -- ]
#   need to instead of real lis, use sorted list throughout [ -- DONE -- ]

import math

### -- BASIC FUNCTIONS -- ###
# List with Frequency Accounted
def calcListFreq(list, freq): 
    newList = []
    i = 0
    for frequency in freq:
        for j in range(frequency):
            newList.append(list[i])
        i += 1
    return newList

# Summation Calculator Function
def calcSum(list): 
    sum = 0
    for items in list:
        sum += items
    return sum

# Summation for Squared Values Calculator Function
def calcSquaredList(list): #
    newList = []
    for elem in list:
        newList.append(elem ** 2)
    return newList


# -- VALUES -- #
    # (test lists for now)
list1 = [22, 23, 21, 24, 25, 26] 
list2 = [2, 3, 4, 1, 5, 2]

REAL_LIST = list1
if (list2 != None):
    REAL_LIST = calcListFreq(list1, list2)
REAL_LIST.sort()

LENGTH = len(REAL_LIST)
SUM_OF_X = calcSum(REAL_LIST)
SUM_OF_X2 = calcSum(calcSquaredList(REAL_LIST))


### -- 1-VAR STATS -- ###
# Calculating the Mean
def calcMean():
    mean = SUM_OF_X / LENGTH
    return mean

# Calculating the Percentile (used to find Q1, med, and Q3)
def calcPercentile(percentile): 
    place = (percentile * LENGTH) / 100
    if place != int(place): # checks if the number is whole
        return REAL_LIST[int(place)]
    result = (REAL_LIST[int(place-1)] + REAL_LIST[int(place)]) / 2
    return result

# Calculating standard deviation
def calcStadDev(samplePopulation, mean):
    listXminusMean = []
    for elems in REAL_LIST:
        listXminusMean.append(elems - mean)
    standardDeviation = calcSum(calcSquaredList(listXminusMean))
    if samplePopulation == "sample":
        standardDeviation /= LENGTH - 1
    else:
        standardDeviation /= LENGTH
    standardDeviation = math.sqrt(standardDeviation)
    return standardDeviation

# Calculation Inter-Quarile Range
def calcIQR(q1, q3):
    return (q3 - q1)

# Calculating Outliers (returns list with all index values where an outlier is)
def calcOutliers(q1, q3, iqr):
    indexValues = []
    outQ1 = q1 - (1.5 * iqr)
    outQ3 = q3 + (1.5 * iqr)
    for i in range(LENGTH):
        if REAL_LIST[i] < outQ1 or REAL_LIST[i] > outQ3:
            indexValues.append(i)
    return indexValues



### -- PRINTING RESULTS for 1-VAR STATS -- ###
## [ VARIABLES ] ## 
MEAN = calcMean()
    # + sum of x and sum of x squared
SAMPLE_STANDARD_DEVIATION = calcStadDev("sample", MEAN)
POPULATION_STANDARD_DEVIATION = calcStadDev("population", MEAN)
    # n = length
MIN = REAL_LIST[0]
MAX = REAL_LIST [LENGTH - 1]
Q1 = calcPercentile(25)
MEDIAN = calcPercentile(50)
Q3 = calcPercentile(75)
SAMPLE_VARIANCE = calcStadDev("sample", MEAN) ** 2
POPULATION_VARIANCE = calcStadDev("population", MEAN) ** 2

## [ PRINTING (old) ] ## 
print("Mean: " + str(calcMean()))
print("Sum of x: " + str(SUM_OF_X))
print("Sum of x squared: " + str(SUM_OF_X2))
print("Sample Standard Deviation: " + str(calcStadDev("sample", calcMean())))
print("Population Standard Deviation: " + str(calcStadDev("population", calcMean())))
print("n: " + str(LENGTH))
print("Minimum X: " + str(REAL_LIST[0]))
print("Q1: " + str(calcPercentile(25))) 
print("Median: " + str(calcPercentile(50)))
print("Q3: " + str(calcPercentile(75)))
print("Maximum X: " + str(REAL_LIST[LENGTH-1]))
print("Sample Variance: " + str(calcStadDev("sample", calcMean()) ** 2))
print("Population Variance: " + str(calcStadDev("population", calcMean()) ** 2))