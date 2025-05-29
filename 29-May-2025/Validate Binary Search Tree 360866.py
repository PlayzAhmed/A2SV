# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):

        def inOrder(node):
            if not node:
                return []

            return inOrder(node.left) + [node.val] + inOrder(node.right)

        tree = inOrder(root)
        return sorted(list(set(tree))) == tree
        