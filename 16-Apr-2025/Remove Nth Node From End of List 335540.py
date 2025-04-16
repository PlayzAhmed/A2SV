# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next

        n = l - n

        i = 0
        cur = head
        prev = cur

        if n == 0:
            return head.next

        while i <= n:
            if i == n:
                prev.next = cur.next
                break

            prev = cur
            cur = cur.next
            i += 1

        
        return head

        