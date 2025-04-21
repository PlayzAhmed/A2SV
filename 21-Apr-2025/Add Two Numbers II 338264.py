# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head):
        cur = head
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev

    def addTwoNumbers(self, l1, l2):
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        res = ListNode(0)
        cur = res
        h = 0

        while l1 or l2:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + h
            h = 0
            if s >= 10:
                h = 1
                s -= 10

            cur.next = ListNode(s)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if h:
            cur.next = ListNode(1)

        return self.reverse(res.next)

        