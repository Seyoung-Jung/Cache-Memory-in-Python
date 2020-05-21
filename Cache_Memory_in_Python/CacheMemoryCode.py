from random import *
from time import *


class CircularQueue:

    def __init__(self, num):
        self.queue = list()
        self.front = 0
        self.rear = 0
        self.maxSize = num

    def enqueue(self, data):
        if self.size() == self.maxSize - 1:
            return False
        self.queue.append(data)
        self.rear = (self.rear + 1) % self.maxSize
        return True

    def dequeue(self):
        if self.size() == 0:
            return False
        data = self.queue[self.front]
        self.front = (self.front + 1) % self.maxSize
        return data

    def size(self):
        if self.rear >= self.front:
            return (self.rear - self.front)
        return (self.maxSize - (self.front - self.rear))



infoList = {}

L1 = CircularQueue(5)
L2 = CircularQueue(20)
L3 = CircularQueue(200)
ram = CircularQueue(500)
hardDisk = range(1,5001)
hit = []

for i in range(10):
    input = [random(1,5000)]
    if input[1] in L1:
        input.append(0.1)
        hit.append(1)
    elif input[1] in L2:
        input.append(0.2)
        if L1.size() == 5: L1.dequeue()
        L1.enqueue([keyindex, index, input[1], input[2]])
        hit.append(1)
    elif input[1] in L3:
        input.append(0.3)
        if L2.size() == 20: L2.dequeue()
        L2.enqueue([keyindex, index, input[1], input[2]])
        if L1.size() == 5: L1.dequeue()
        L1.enqueue([keyindex, index, input[1], input[2]])
        hit.append(1)
    elif input[1] in ram:
        input.append(1.3)
        if L3.size() == 200: L3.dequeue()
        L3.enqueue([keyindex, index, input[1], input[2]])
        if L2.size() == 20: L2.dequeue()
        L2.enqueue([keyindex, index, input[1], input[2]])
        if L1.size() == 5: L1.dequeue()
        L1.enqueue([keyindex, index, input[1], input[2]])
        hit.append(0)
    else:
        input.append(4.3)
        if L3.size() == 200: L3.dequeue()
        L3.enqueue([keyindex, index, input[1], input[2]])
        if L2.size() == 20: L2.dequeue()
        L2.enqueue([keyindex, index, input[1], input[2]])
        if L1.size() == 5: L1.dequeue()
        L1.enqueue([keyindex, index, input[1], input[2]])
        hit.append(0)
    infoList[keyindex?] = [input[1], input[2], clock(), 현재 있는 곳?, 히트여부?]


hitRatio = 0
for i in hit:
    hitRatio += i

hitRatio /= len(hit)
missRatio = 1 - hitRatio

