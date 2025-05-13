# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        cur = root
        while cur:
            if cur.val < val:
                cur = cur.right
            elif cur.val > val:
                cur = cur.left
            else:
                return cur

        return
        