# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        mp = {None: None}
        cur = head

        while cur:
            mp[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur:
            copy = mp[cur]
            copy.next = mp[cur.next]
            copy.random = mp[cur.random]
            cur = cur.next

        return mp[head]
        