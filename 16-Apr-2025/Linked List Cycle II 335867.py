# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        cycle = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                cycle = True
                break

        if cycle:
            while slow != head:
                head = head.next
                slow = slow.next

            return slow

        