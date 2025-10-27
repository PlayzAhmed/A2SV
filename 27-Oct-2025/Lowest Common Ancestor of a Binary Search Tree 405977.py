# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        p = p.val
        q = q.val

        while root:
            print(root.val)
            if root.val == q or root.val == p or (min(p,q) < root.val and max(p,q) > root.val):
                return root

            if max(q,p) < root.val:
                root = root.left
            elif max(q,p) > root.val:
                root = root.right