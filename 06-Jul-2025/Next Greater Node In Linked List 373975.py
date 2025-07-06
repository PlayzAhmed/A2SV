# Problem: Next Greater Node In Linked List - https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        st = []

        cur = head

        while cur:
            while st and st[-1].val < cur.val:
                node = st.pop()
                node.val = cur.val

            st.append(cur)
            cur = cur.next

        for node in st:
            node.val = 0

        cur = head
        ans = []

        while cur:
            ans.append(cur.val)
            cur = cur.next

        return ans