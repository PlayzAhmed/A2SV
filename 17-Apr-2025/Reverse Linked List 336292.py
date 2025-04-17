# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head:
            dummy = ListNode(head.val)
            head = head.next
        else:
            return

        while head:
            temp = ListNode(head.val)
            temp.next = dummy
            dummy = temp
            head = head.next

        return dummy