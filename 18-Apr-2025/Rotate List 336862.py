# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        temp = head
        tail = None
        n = 0
        while temp:
            n += 1
            tail = temp
            temp = temp.next

        if n < 2:
            return head

        k %= n

        if k == 0:
            return head

        cur = head
        i = 0
        k = n - k - 1

        while cur and i < k:
            cur = cur.next
            i += 1

        tail.next = head
        head = cur.next
        cur.next = None

        return head