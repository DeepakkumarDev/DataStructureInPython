from array import *
import numpy as np
arr1=array('i',[1,2,3,4,5,6])
arr2=array('d',[1.3,1.4])
arr1.insert(2,89)
arr1.remove(6)
# print(arr1)
# print(arr2)


def traverseArray(array):
    for i in array:
        print(i)

# traverseArray(arr1)

def accessElement(array,index):
    if index>=len(array):
        print('There is not any element in this index')
    else:
        print(array[index])
# accessElement(arr1,6)

def searchInArray(array,value):
    for i in array:
        if i==value:
            return array.index(value)
    return "The element does not exist in this array"

# print(searchInArray(arr1,0))


twoDArray=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
newTwoDArray=np.insert(twoDArray,0,[[1,2,3,4]],axis=1)
newTwoDArray=np.insert(twoDArray,0,[[1,2,3,4]],axis=0)

# print(twoDArray)
# print(newTwoDArray)

def accessElements(array,rowIndex,colIndex):
    if rowIndex>=len(array) and colIndex>=len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])

# accessElements(twoDArray,2,2)


# print(len(newTwoDArray[0]))



def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=" ")
        print()

traverseTDArray(twoDArray)