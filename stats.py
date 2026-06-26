# -- BASIC FUNCTIONS -- #
def calcListFreq(list, freq):
    newList = []
    i = 0
    for frequency in freq:
        for j in range(frequency):
            newList.append(list[i])
        i += 1
    return newList

def calcSum(list):
    sum = 0
    for items in list:
        sum += items
    return sum

# -- VALUES -- #
    # (test lists for now)
list1 = [22, 23, 21, 24, 25, 26] 
list2 = [2, 3, 4, 1, 5, 2]
REAL_LIST = list1

if (list2 != None):
    REAL_LIST = calcListFreq(list1, list2)

LENGTH = len(REAL_LIST)
SUM_OF_X = calcSum(REAL_LIST)
SUM_OF_X2 = calcSum(REAL_LIST) # MUST FIX


# -- 1-VAR STATS -- #
def calcMean():
    mean = SUM_OF_X / LENGTH
    return mean

def calcMedian(): # MUST FIX
    withFreqList = []
    if LENGTH % 2 != 0:
        return REAL_LIST[int(LENGTH/2)]
    median = (REAL_LIST[int(LENGTH/2)] + REAL_LIST[int(LENGTH/2)+1]) / 2
    return median
    



print(calcMedian())
