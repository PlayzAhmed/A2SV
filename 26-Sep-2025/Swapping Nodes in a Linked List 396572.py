# Problem: Swapping Nodes in a Linked List - https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        return self.buildLinkedList(self.readLinkedList(head, k))

    def readLinkedList(self, head, k):
        ans = []
        cur = head

        while cur:
            ans.append(cur.val)
            cur = cur.next

        ans[-k], ans[k-1] = ans[k-1], ans[-k]

        return ans

    def buildLinkedList(self, arr):
        dummy = ListNode()
        cur = dummy

        for x in arr:
            cur.next = ListNode(x)
            cur = cur.next

        return dummy.next
        