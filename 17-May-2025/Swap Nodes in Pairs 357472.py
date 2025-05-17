# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            temp = cur.next.next
            nxt = cur.next

            nxt.next = cur
            cur.next = temp
            prev.next = nxt

            prev = cur
            cur = temp

        return dummy.next