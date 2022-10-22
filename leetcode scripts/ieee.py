# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
#import scipy
import sys
import copy
budget = 0
def printSelection(arr):
    arr.sort(key=lambda x: x[2])
    for player in arr:
        print(player[1])

def checkSum(arr):
    currSum = 0
    for player in arr:
        if len(player) > 0:
            currSum += int(player[0])
    if currSum < budget:
        return 1
    elif currSum == budget:
        return 0
    else:
        return -1

def getSum(arr):
    sum = 0
    for i in arr:
        if len(i) > 0:
            sum += int(i[0])
    return sum

def selectGreedy(wages, position, playerIndex, selection):
    selection2 = copy.deepcopy(selection)
    withItem = 0
    withoutItem = 0
    largerSelection = []
    for i in range(position,5):
        selection[i] = wages[i][0]
        playerCount = len(wages[i])
        if playerCount > 1:
            for playerNum in range(0, playerCount-1):
                withItem = selectGreedy(wages, i+1, playerNum, selection)
                withoutItem = selectGreedy(wages, i, playerNum + 1, selection2)
                if withItem > withoutItem:
                    largerSelection = selection
                else:
                    largerSelection = selection2
        else:
            selection2 = copy.deepcopy(selection)
    if position == 5:
        sum = checkSum(selection)
        if sum >= 0:
            return getSum(selection)
        else:
            return -1
    else:
        if playerIndex >= len(arr[position]):
            return -1
        else:
            selection[position] = arr[position][playerIndex]
            sum = checkSum(selection)
            if sum == 0:
                return -1
            elif sum == 1:
                return selectGreedy(arr, position+1, 0, selection)
            else:
                selection[position] = []
                return selectGreedy(arr, position, playerIndex + 1, selection)
            

def maximizeBudget(wages, selection):
    selection2 = copy.deepcopy(selection)
    withItem = 0
    withoutItem = 0
    largerSelection = []
    for i in range(5):
        selection[i] = wages[i][0]
        playerCount = len(wages[i])
        if playerCount > 1:
            for playerNum in range(0, playerCount-1):
                withItem = selectGreedy(wages, i+1, playerNum, selection)
                withoutItem = selectGreedy(wages, i, playerNum + 1, selection2)
                if withItem > withoutItem:
                    largerSelection = selection
                else:
                    largerSelection = selection2
        else:
            selection2 = copy.deepcopy(selection)
    
    printSelection(largerSelection)
        

def sortMax(arr):
    for i in arr:
        i.sort(reverse=True)

def main(input):
    wages = [[],[],[],[],[]]
    selection = [[],[],[],[],[]]
    global budget 
    budget = int(input[0])
    pos = 1
    for i in range(5):
        lines = int(input[pos])
        for j in range(lines):
            pos += 1
            player = input[pos].split(" ")
            wages[i].append([int(player[1]), player[0], i])
        pos += 1    
    
    
    sortMax(wages)
    
    wages.sort(reverse=True)
    #wages.sort(key=lambda x: len(x))
    
    #selectGreedy(wages, 0, 0, selection)
    maximizeBudget(wages, selection)


input = ['235000', '3', 'curry 40000', 'nash 20000', 'johnson 10000', '3', 'jordan 50000', 'wade 20000', 'bryant 80000', '1', 'james 30000', '2', 'duncan 60000', 'sambadi 65000', '1', 'oneal 100000']


if __name__ == '__main__':
    #input = []
    #for line in sys.stdin:
    #    input.append(line.strip(" \r\n"))
    main(input)
