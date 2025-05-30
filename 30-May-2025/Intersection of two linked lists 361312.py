# Problem: Intersection of two linked lists - https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        freq = defaultdict(bool)

        cur = headA

        while cur:
            freq[cur] = True
            cur = cur.next

        cur = headB

        while cur:
            if freq[cur]:
                return cur

            cur = cur.next

        return None
        