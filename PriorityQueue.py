#! /usr/bin/env python3
########################################
# CS63: Artificial Intelligence, Lab 1
# Spring 2022, Swarthmore College
########################################

class PriorityQueue(object):
    def __init__(self):
        """
        Represent the min priority queue as a heap, which is a complete
        binary tree represented as a list.
        """
        self.heap = []
    def isEmpty(self):
        return len(self.heap) == 0
    def getSize(self):
        return len(self.heap)
    def left(self, index):
        return 2*index + 1
    def right(self, index):
        return 2*index + 2
    def parent(self, index):
        return (index-1)//2
    def insert(self, priority, item):
        self.heap.append((priority, item))
        self.bubbleUp(self.getSize()-1)
    def bubbleUp(self, index):
        if index != 0:
            p_index = self.parent(index)
            if self.heap[index][0] < self.heap[p_index][0]:
                self.swap(index, p_index)
                self.bubbleUp(p_index)
    def remove(self):
        if self.getSize() == 0:
            raise RuntimeError("can't remove from an empty PQ")
        removed_item = self.heap[0][1]
        last_index = self.getSize()-1
        self.heap[0] = self.heap[last_index]
        self.heap.pop(last_index)
        self.bubbleDown(0)
        return removed_item
    def bubbleDown(self, index):
        l = self.left(index)
        if l < self.getSize():
            # has a left child
            minIndex = l
            r = self.right(index)
            if r < self.getSize():
                # also has a right child, see if its priority is lower
                if self.heap[r][0] < self.heap[l][0]:
                    minIndex = r
            if self.heap[minIndex][0] < self.heap[index][0]:
                self.swap(index, minIndex)
                self.bubbleDown(minIndex)
    def swap(self, i1, i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]
        
if __name__ == '__main__':
    pq = PriorityQueue()
    try:
        result = pq.remove()
    except RuntimeError:
        print("Successfully threw an error when removing from empty pq")
    print("Inserting 5 letters as test items")
    pq.insert(20, 'e')
    pq.insert(10, 'd')
    pq.insert(7, 'c')
    pq.insert(3, 'a')
    pq.insert(5, 'b')
    print("Size of pq is:", pq.getSize())
    print("Remove items until pq is empty, should be in alpahbetic order")
    while not pq.isEmpty():
        item = pq.remove()
        print("Removed item:", item)
    print("Size is now:", pq.getSize())
    
