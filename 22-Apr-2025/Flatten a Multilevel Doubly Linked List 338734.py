# Problem: Flatten a Multilevel Doubly Linked List - https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/?envType=problem-list-v2&envId=linked-list

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        dummy = Node(None, None, None, None)
        cur = head
        temp = dummy

        self.getting_child_val(cur, None, temp)
        if dummy.next:
            dummy.next.prev = None
        return dummy.next

    def getting_child_val(self, cur, prev, temp):
        cur = cur
        temp = temp
        prev = prev
        while cur:
            temp.next = Node(cur.val, temp, None, None)
            temp = temp.next

            child = cur.child

            if child:
                temp = self.getting_child_val(child, cur, temp)
            
            prev = temp
            cur = cur.next
            

        return temp
        