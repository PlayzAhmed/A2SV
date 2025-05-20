# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if left == right:
            return head

        head = ListNode(0, head)
        cur = head
        i = 0
        dummy = None
        tail = None
        prev = None

        while cur and i <= right:
            if i < left:
                prev = cur
            elif i == left:
                tail = ListNode(cur.val, dummy)
                dummy = tail
            else:
                dummy = ListNode(cur.val, dummy)

            cur = cur.next
            i += 1

        prev.next = dummy
        tail.next = cur

        return head.next
        