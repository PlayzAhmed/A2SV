# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        dummy = ListNode()
        cur = dummy

        for i, node in enumerate(lists):
            if node: heappush(heap, (node.val, i, node))

        while heap:
            val, i, node = heappop(heap)
            cur.next = node
            cur = cur.next
            node = node.next
            if node: heappush(heap, (node.val, i, node))

        return dummy.next