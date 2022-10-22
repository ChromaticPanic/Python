import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#
def choosePivot(start, end):
    pivot = end + (start - end) // 2
    assert(pivot >= start and pivot <= end)
    return pivot
    
def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    
def quickPartition(indexArr, arr, start, end):
    highIndex = start + 1
    pivot = arr[start]
        
    for currPos in range( start + 1, end): 
        if(int(arr[currPos][0]) < int(pivot[0])):                         
            swap(arr, currPos, highIndex)
            swap(indexArr, currPos, highIndex)
            highIndex += 1
        
    swap(arr, start, highIndex-1)
    swap(indexArr, start, highIndex-1)
    return highIndex-1
    
def quickSort(indexArr, arr, start, end):
    if ( 2 > (end - start) ):   # base case, if there are only 2 items. swap if necessary
        if (end < len(arr) and int(arr[end][0]) < int(arr[start][0])):
            swap(arr, end, start)
            swap(indexArr, end, start)
            
    else:
        pivot = choosePivot(start, end)
        swap(arr, pivot, start)
        swap(indexArr, pivot, start)
        pivot = quickPartition(indexArr, arr, start, end)
        quickSort( indexArr, arr, start, pivot)
        quickSort( indexArr, arr, pivot + 1, end)
    
    
def countSort(arr):
    # Write your code here
    indexArr = list(range(len(arr)))
    print(indexArr)
    quickSort(indexArr, arr, 0, len(arr)-1)
    half = len(arr) // 2
    output = ""
    for i in range(len(arr)):
        if (indexArr[i] <= half):
            output += "- "
        else:
            output += arr[indexArr[i]][1] + " "
    print(output)



if __name__ == '__main__':
    arr = [['0','ab'],['6','cd'],['0','ef'],['6','gh'],['4','ij'],['0','ab'],['6','cd'],['0','ef'],['6','gh'],['0','ij'],['4','that'],['3','be'],['0','to'],['1','be'],['5','question'],['1','or'],['2','not'],['4','is'],['2','to'],['4','the']]
    countSort(arr)