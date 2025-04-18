# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class ListNode():
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = self.head

    def get(self, index):
        cur = self.head
        i = 0
        while cur and i <= index:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1

        return -1

        

    def addAtHead(self, val):
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head = node

        

    def addAtTail(self, val):
        node = ListNode(val)
        if not self.tail:
            self.tail = node
            self.head = node
            return

        self.tail.next = node
        self.tail = self.tail.next
            
        

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return
        
        if not self.head:
                    return
        
        cur = self.head
        prev = None
        i = 0
        while cur:
            if i == index:
                node = ListNode(val)
                node.next = cur
                prev.next = node
                return

            i += 1
            prev = cur
            cur = cur.next

        if index == i:
            self.addAtTail(val)

    def deleteAtIndex(self, index):
        i = 0
        cur = self.head
        prev = None

        while cur:
            if i == index:
                if prev:
                    prev.next = cur.next
                    if cur == self.tail:
                        self.tail = prev
                else:
                    self.head = self.head.next
                break

            prev = cur
            cur = cur.next
            i += 1
