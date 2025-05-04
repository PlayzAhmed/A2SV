# Problem: Remove Nodes From Linked List - https://leetcode.com/problems/remove-nodes-from-linked-list/description/?envType=problem-list-v2&envId=recursion

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        head = self.reverseLinkedList(head)
        
        cur = head
        prev = None
        mx = cur.val

        while cur:
            if cur.val < mx:
                if prev:
                    prev.next = cur.next
                else:
                    head = cur.next
            else:
                prev = cur
                
            cur = cur.next
            if cur:
                mx = max(cur.val, mx)

        return self.reverseLinkedList(head)

    def reverseLinkedList(self, head):
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
        