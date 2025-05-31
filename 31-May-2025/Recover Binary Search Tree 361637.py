# Problem: Recover Binary Search Tree - https://leetcode.com/problems/recover-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        self.inorder = []

        def dfs(node):
            if not node: return
            
            dfs(node.left)
            self.inorder.append(node)
            dfs(node.right)

        dfs(root)

        sorted_tree = sorted(node.val for node in self.inorder)

        for i in range(len(sorted_tree)):
            self.inorder[i].val = sorted_tree[i]

            