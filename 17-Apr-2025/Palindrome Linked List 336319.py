# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        r = ListNode(head.val)
        cur = head.next
        while cur:
            temp = ListNode(cur.val)
            temp.next = r
            r = temp
            cur = cur.next

        while r and head:
            if r.val == head.val:
                r = r.next
                head = head.next
            else:
                return False

        return True
        