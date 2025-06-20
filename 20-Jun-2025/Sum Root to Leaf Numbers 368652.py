# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        ans = [0]
        def dfs(node, num=0):
            if not node or (not node.left and not node.right):
                ans[0] += num * 10 + node.val
                return

            if node.left:
                dfs(node.left, node.val if not num else num * 10 + node.val)
            if node.right:
                dfs(node.right, node.val if not num else num * 10 + node.val)

        dfs(root)
        return ans[0]
        