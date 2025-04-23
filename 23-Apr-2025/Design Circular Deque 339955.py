# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque(object):

    def __init__(self, k):
        self.queue = []
        self.max = k
        

    def insertFront(self, value):
        if len(self.queue) < self.max:
            self.queue.insert(0, value)
            return True
        return False
        

    def insertLast(self, value):
        if len(self.queue) < self.max:
            self.queue.append(value)
            return True
        return False

    def deleteFront(self):
        if self.queue:
            self.queue.pop(0)
            return True
        return False

    def deleteLast(self):
        if self.queue:
            self.queue.pop()
            return True
        return False

    def getFront(self):
        return self.queue[0] if self.queue else -1
        

    def getRear(self):
        return self.queue[-1] if self.queue else -1
        

    def isEmpty(self):
        return not self.queue
        

    def isFull(self):
        return len(self.queue) == self.max
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()