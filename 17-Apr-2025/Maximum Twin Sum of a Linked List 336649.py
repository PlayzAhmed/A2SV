# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        s = []
        slow = fast = head

        while fast:
            s.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        res = 0

        while slow:
            res = max(res, slow.val+s.pop())
            slow = slow.next

        return res
        