import sys
import array
from collections import deque
import heapq


def dq():
    q = deque()
    q.append(1)
    q.append(2)
    q.popleft()


def arr():
    a = array.array('i', (1, 2, 3))
    a.append(4)
    a[0]


def hp(size):
    h = [] * size
    priority = 1
    id = 1
    item = None
    heapq.heappush(h, (priority, id, item))
    heapq.heappush(h, 2)
    heapq.heappop(h)

def heapify(x):
    heapq.heapify(x)

def heapsort(iterable):
     h = []
     for value in iterable:
         heapq.heappush(h, value)
     return [heapq.heappop(h) for i in range(len(h))]

def get_subsets(s):
    if len(s) == 0:
        return [[]]
    else:
        subsets = get_subsets(s[1:])
        item = s[0]
        new_subsets = []
        for subset in subsets:
            new_subset = []
            new_subset.extend(subset)
            new_subset.append(item)
            new_subsets.append(new_subset)
        subsets.extend(new_subsets)
        return subsets



def main(input):
    pass

if __name__ == '__main__':
    input = []
    for line in sys.stdin:
        input.append(line.strip(" \r\n"))
    main(input)