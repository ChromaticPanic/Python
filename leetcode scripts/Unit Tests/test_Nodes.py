import pytest
import sys
import random
sys.path.append('../')
from NodeBased import Stack
from NodeBased import Queue
from NodeBased import OrderedList
from NodeBased import NodeItem


def test_stack():
    myStack = Stack()
    assert myStack.pop() == None
    myStack.push(1)
    myStack.push(2)
    assert myStack.pop() == 2
    assert myStack.pop() == 1
    assert myStack.pop() == None

def test_queue():
    myQueue = Queue()
    assert myQueue.dequeue() == None
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    assert myQueue.dequeue() == 1
    assert myQueue.dequeue() == 2
    assert myQueue.dequeue() == None

def test_OrderedList_simple():
    myOrderedList = OrderedList()
    assert myOrderedList.remove(1) == None
    newItem = NodeItem()
    newItem.value = 1
    myOrderedList.orderedInsert(newItem)
    assert myOrderedList.remove(0).value == 1
    myOrderedList.orderedInsert(newItem)
    assert myOrderedList.removeLast().value == 1
    assert myOrderedList.size() == 0

def setup_OrderedList():
    values = [5, 3, 1, 2, 4, 10, 8, 6, 7, 9]
    myOrderedList = OrderedList()
    for v in values:
        newItem = NodeItem()
        newItem.value = v
        myOrderedList.orderedInsert(newItem)
    return myOrderedList

def test_OrderedList_remove():
    myOrderedList = setup_OrderedList()
    assert myOrderedList.size() == 10
    assert myOrderedList.remove(4).value == 5
    assert myOrderedList.remove(0).value == 1
    assert myOrderedList.remove(7).value == 10
    assert myOrderedList.remove(6).value == 9
    assert myOrderedList.size() == 6

def test_OrderedList_removelast():
    myOrderedList = setup_OrderedList()
    out = str(myOrderedList)
    assert myOrderedList.removeLast().value == 10
    assert myOrderedList.removeLast().value == 9
    assert myOrderedList.removeLast().value == 8
    assert myOrderedList.removeLast().value == 7
    assert myOrderedList.removeLast().value == 6
    assert myOrderedList.removeLast().value == 5
    assert myOrderedList.removeLast().value == 4
    assert myOrderedList.removeLast().value == 3
    assert myOrderedList.removeLast().value == 2
    assert myOrderedList.removeLast().value == 1
    assert myOrderedList.removeLast() == None
    assert myOrderedList.size() == 0

def test_OrderedList_mixedremove():
    myOrderedList = setup_OrderedList()
    assert myOrderedList.remove(0).value == 1
    assert myOrderedList.remove(0).value == 2
    assert myOrderedList.remove(0).value == 3
    assert myOrderedList.remove(0).value == 4
    assert myOrderedList.remove(0).value == 5
    assert myOrderedList.removeLast().value == 10
    assert myOrderedList.removeLast().value == 9
    assert myOrderedList.removeLast().value == 8
    assert myOrderedList.removeLast().value == 7
    assert myOrderedList.removeLast().value == 6
    assert myOrderedList.removeLast() == None
    assert myOrderedList.size() == 0

def test_OrderedList_removemiddle():
    myOrderedList = setup_OrderedList()
    assert myOrderedList.remove(2).value == 3
    assert myOrderedList.remove(2).value == 4
    assert myOrderedList.remove(2).value == 5
    assert myOrderedList.remove(2).value == 6
    assert myOrderedList.removeLast().value == 10
    assert myOrderedList.removeLast().value == 9
    assert myOrderedList.removeLast().value == 8
    assert myOrderedList.removeLast().value == 7
    assert myOrderedList.size() == 2

    

if __name__ == '__main__':
    test_OrderedList()
