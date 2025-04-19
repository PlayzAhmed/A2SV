# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class ListNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        nxt.prev = prev.next = node
        node.next, node.prev = nxt, prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)