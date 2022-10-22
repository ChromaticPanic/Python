import os 
import sys


class Stack:
    def __init__(self):
        self.__array = []
        self.__size = 0

    def push(self, item):
        self.__array.append(item)
        self.__size += 1
        
    def pop(self):
        self.__size -= 1
        return self.__array.pop()

    def size(self):
        return self.__size

class Queue:
    def __init__(self):
        self.__array = []
        self.__size = 0

    def enqueue(self, item):
        self.__array.append(item)
        self.__size += 1
        
    def dequeue(self):
        self.__size -= 1
        return self.__array.pop()

    def size(self):
        return self.__size

class pQueue:
    def __init__(self):
        self.__array = []


class Tree:
    def __init__(self):
        self.__array = []

class BST:
    def __init__(self):
        self.__array = []


class HashMap:
    def __init__(self, size: int):
        self.__array = []


class HashMap:
    def __init__(self, size: int):
        if size > 0:
            self.__size = size
            self.__array = [None] * size

    def hash(self, item):
        return hash(item) % self.__size

    def add(self, item):
        self.__array[self.hash(item)] = item

    def remove(self, item):
        self.__array[self.hash(item)] = None

    def contains(self, item):
        return self.__array[self.hash(item)] == item

    def size(self):
        return self.__size

    def __str__(self):
        return str(self.__array)

class BinarySearch:
    def __init__(self, array: list):
        self.__array = array

    def search(self, item):
        return self.__binarySearch(item, 0, len(self.__array) - 1)

    def __binarySearch(self, item, low, high):
        if high < low:
            return -1

        mid = high + (low - high) // 2

        if item == self.__array[mid]:
            return mid
        elif item < self.__array[mid]:
            return self.__binarySearch(item, low, mid - 1)
        else:
            return self.__binarySearch(item, mid + 1, high)