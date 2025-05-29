# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):

        def dfs(node1, node2):
            if node1 and node2 and node1.val == node2.val:
                return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
            elif not (node1 or node2):
                return True
            return False
        
        return dfs(root.left, root.right)

        