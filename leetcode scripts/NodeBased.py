import os 
import sys


class NodeSingle:
    def __init__(self):
        self.next = None
        self.item = None

    def __str__(self):
        return str(self.item)


class NodeDouble:
    def __init__(self):
        self.left = None
        self.right = None
        self.item = None

class NodeItem:
    def __init__(self):
        self.value = None
        self.sortParams = []
    
    def __eq__(self, other):
        result = False
        if other != None:
            result = self.value == other.value
        return result

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
        return str(self.value)
    
class Stack:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def push(self, item):

        if item != None:
            newNode = NodeSingle()
            newNode.item = item

            if self.__size == 0:
                self.__head = newNode
            else:
                newNode.next = self.__head
                self.__head = newNode

            self.__size += 1
        
    def pop(self):

        result = None

        if self.__size > 0:
            result = self.__head.item
            self.__head = self.__head.next
            self.__size -= 1

        return result

    def size(self):
        return self.__size

class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, item):

        if item != None:
            newNode = NodeSingle()
            newNode.item = item

            if self._size == 0:
                self._head = newNode
                self._tail = self._head
            else:
                self._tail.next = newNode
                self._tail = newNode

            self._size += 1
        
    def dequeue(self):

        result = None

        if self._size > 0:
            result = self._head.item
            self._head = self._head.next
            self._size -= 1

        return result

    def size(self):
        return self._size

class PriorityQueue(Queue):
    def __init__(self):
        super().__init__()

    def enqueue(self, item):
        if item != None:
            newNode = NodeSingle()
            newNode.item = item

            if self._size == 0:
                self._head = newNode
                self._tail = self._head
            else:
                if self._head.item < newNode.item:
                    newNode.next = self._head
                    self._head = newNode
                else:
                    current = self._head
                    while current.next != None and current.next.item < newNode.item:
                        current = current.next

                    newNode.next = current.next
                    current.next = newNode

            self._size += 1

class OrderedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def addLast(self, item):
        if item != None:
            newNode = NodeSingle()
            newNode.item = item

            if self._size == 0:
                self._head = newNode
                self._tail = self._head
            else:
                self._tail.next = newNode
                self._tail = newNode

            self._size += 1

    def orderedInsert(self, item):

        if item != None:
            newNode = NodeSingle()
            newNode.item = item

            if self._size == 0:
                self._head = newNode
                self._tail = self._head
            else:
                curr = self._head
                prev = None
                while curr != None and curr.item < newNode.item:
                    prev = curr
                    curr = curr.next
                if prev == None:
                    newNode.next = self._head
                    self._head = newNode
                else:
                    newNode.next = curr
                    prev.next = newNode
                if curr == None:
                    self._tail = newNode
                    
            self._size += 1

    def insert(self, item, position: int):
        if item != None and position >= 0 and position <= self._size:
            newNode = NodeSingle()
            newNode.item = item

            if position == 0:
                newNode.next = self._head
                self._head = newNode
            else:
                current = self._head
                for i in range(position - 1):
                    current = current.next

                newNode.next = current.next
                current.next = newNode

            self._size += 1

    def remove(self, position: int):
        result = None

        if position >= 0 and position < self._size:
            if position == 0:
                result = self._head.item
                self._head = self._head.next
            else:
                current = self._head
                for i in range(position - 1):
                    current = current.next

                result = current.next.item
                current.next = current.next.next

            self._size -= 1

        return result

    def removeLast(self):
        result = None

        if self._size > 0:
            result = self._tail.item
            current = self._head
            while current.next != None and current.next != self._tail:
                current = current.next

            self._tail = current
            self._tail.next = None
            self._size -= 1

        return result

    def find(self, item):
        result = None

        current = self._head
        while current != None and current.item != item:
            current = current.next

        if current != None:
            result = current.item

        return result

    def findPosition(self, item):
        result = 0

        current = self._head
        while current != None and current.item != item:
            current = current.next
            result += 1

        if current == None:
            result = -1

        return result

    def size(self):
        return self._size

    def __str__(self):
        result = ""

        current = self._head
        while current != None:
            result += str(current.item) + " "
            current = current.next

        return result

class DoubleLinkOrderedList():
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def addLast(self, item):
        if item != None:
            newNode = NodeDouble()
            newNode.item = item

            if self._size == 0:
                self._head = newNode
                self._tail = self._head
            else:
                self._tail.next = newNode
                newNode.prev = self._tail
                self._tail = newNode

            self._size += 1

    def insert(self, item, position: int):
        if item != None and position >= 0 and position <= self._size:
            newNode = NodeDouble()
            newNode.item = item

            if position == 0:
                newNode.next = self._head
                self._head.prev = newNode
                self._head = newNode
            else:
                current = self._head
                for i in range(position - 1):
                    current = current.next

                newNode.next = current.next
                current.next.prev = newNode
                current.next = newNode
                newNode.prev = current

            self._size += 1

    def orderedInsert(self, item):
        if item != None:
            newNode = NodeDouble()
            newNode.item = item

            if self._size == 0:
                self._head = newNode
                self._tail = self._head
            else:
                curr = self._head
                prev = None
                while curr != None and curr.item < newNode.item:
                    prev = curr
                    curr = curr.next
                if prev == None:
                    newNode.next = self._head
                    self._head.prev = newNode
                    self._head = newNode
                else:
                    newNode.next = curr
                    curr.prev = newNode
                    prev.next = newNode
                    newNode.prev = prev
                if curr == None:
                    self._tail = newNode
                    
            self._size += 1

    def remove(self, position: int):
        result = None

        if position >= 0 and position < self._size:
            if position == 0:
                result = self._head.item
                self._head = self._head.next
                self._head.prev = None
            else:
                current = self._head
                for i in range(position - 1):
                    current = current.next

                result = current.next.item
                current.next = current.next.next
                if current.next != None:
                    current.next.prev = current

            self._size -= 1

        return result

    def removeLast(self):
        result = None

        if self._size > 0:
            result = self._tail.item
            self._tail = self._tail.prev
            self._tail.next = None
            self._size -= 1

        return result

    def find(self, item):
        result = None

        current = self._head
        while current != None and current.item != item:
            current = current.next

        if current != None:
            result = current.item

        return result

    def findPosition(self, item):
        result = 0

        current = self._head
        while current != None and current.item != item:
            current = current.next
            result += 1

        if current == None:
            result = -1

        return result

    def size(self):
        return self._size

    def __str__(self):
        result = ""

        current = self._head
        while current != None:
            result += str(current.item) + " "
            current = current.next

        return result

class BinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def insert(self, item):
        if item != None:
            newNode = NodeDouble()
            newNode.item = item

            if self._size == 0:
                self._root = newNode
            else:
                current = self._root
                
                if item < current.item:
                    if current.left == None:
                        current.left = newNode
                    else:
                        current = current.left
                elif item > current.item:
                    if current.right == None:
                        current.right = newNode
                    else:
                        current = current.right

            self._size += 1

    def remove(self, item):
        result = None

        if self._size > 0:
            if self._root.item == item:
                result = self._root.item
                self._root = None
            else:
                current = self._root
                while current != None:
                    if item < current.item:
                        if current.left != None and current.left.item == item:
                            result = current.left.item
                            current.left = None
                            break
                        else:
                            current = current.left
                    else:
                        if current.right != None and current.right.item == item:
                            result = current.right.item
                            current.right = None
                            break
                        else:
                            current = current.right

        return result

    def searchInorder(self, item):
        result = None

        current = self._root
        while current != None:
            if item < current.item:
                current = current.left
            elif item > current.item:
                current = current.right
            else:
                result = current.item
                break

        return result
    
    def searchPreorder(self, item):
        result = None

        current = self._root
        while current != None:
            if item == current.item:
                result = current.item
                break
            elif item < current.item:
                current = current.left
            else:
                current = current.right

        return result

    def searchPostorder(self, item):
        result = None

        current = self._root
        while current != None:
            if item < current.item:
                current = current.left
            elif item > current.item:
                current = current.right
            else:
                result = current.item
                break

        return result


# class MinHeap:
#     def __init__(self):
#         self.__top = None
#         self.__size = 0

#     def insert(self, item):
#         if item != None:
#             newNode = NodeDouble()
#             newNode.item = item

#             if self.__size == 0:
#                 self.__top = newNode
#             else:
#                 self.__insert(self.__top, newNode)

#             self.__size += 1

#     def __insert(self, parent, child):
#         if parent.left == None:
#             parent.left = child
#         elif parent.right == None:
#             parent.right = child
#         else:
#             if self.__size % 2 == 0:
#                 self.__insert(parent.left, child)
#             else:
#                 self.__insert(parent.right, child)

#     def siftDown(self):

        

#     def remove(self):
#         result = None

#         if self.__size > 0:
#             result = self.__top.item
#             self.__top.item = None
#             self.__size -= 1

#         return result

#     def size(self):
#         return self.__size

    
