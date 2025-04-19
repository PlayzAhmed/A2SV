# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class ListNode():
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node

class MyCircularQueue(object):

    def __init__(self, k):
        self.head = None
        self.tail = self.head
        self.size = 0
        self.maxSize = k
        

    def enQueue(self, value):
        if self.size >= self.maxSize:
            return False

        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

        return True
        

    def deQueue(self):
        if self.size == 0:
            return False

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return True

        cur = self.head

        while cur.next !=  self.tail:
            cur = cur.next

        cur.next = None
        self.tail = cur
        self.size -= 1

        return True
        

    def Front(self):
        if self.size == 0:
            return -1
        else:
            return self.tail.val
        

    def Rear(self):
        if self.size == 0:
            return -1
        else:
            return self.head.val
        

    def isEmpty(self):
        return self.size == 0
        

    def isFull(self):
        return self.size == self.maxSize
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()