# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        greater = ListNode()
        smaller = ListNode()
        cur = head
        smaller_cur = smaller
        greater_cur = greater

        while cur:
            if cur.val >= x:
                greater_cur.next = ListNode(cur.val)
                greater_cur = greater_cur.next
            else:
                smaller_cur.next = ListNode(cur.val)
                smaller_cur = smaller_cur.next

            cur = cur.next

        smaller_cur.next = greater.next
        return smaller.next