# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        cur = head
        
        if not cur or not cur.next:
            return head

        prev = cur
        cur = cur.next

        while cur:
            if cur.val == prev.val:
                cur = cur.next
            else:
                prev.next = prev = cur
                cur = cur.next

        prev.next = cur

        return head

        