# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        res = ListNode()
        cur = res
        hold = 0

        while l1 and l2:
            s = l1.val + l2.val + hold

            if s >= 10:
                hold = 1
                s %= 10
            else:
                hold = 0

            cur.next = ListNode(s)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            s = l1.val + hold

            if s >= 10:
                s %= 10
                hold = 1
            else: 
                hold = 0

            cur.next = ListNode(s)
            cur = cur.next
            l1 = l1.next

        while l2:
            s = l2.val + hold

            if s >= 10:
                s %= 10
                hold = 1
            else: 
                hold = 0

            cur.next = ListNode(s)
            cur = cur.next
            l2 = l2.next

        if hold == 1:
            cur.next = ListNode(1)

        return res.next
        
        