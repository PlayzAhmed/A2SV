# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        ans = []
        def dfs(node, cur=[]):
            if not node.left and not node.right:
                cur.append(str(node.val))
                ans.append("->".join(cur))
                cur.pop()
                return
            
            cur.append(str(node.val))
            if node.left:
                dfs(node.left, cur)

            if node.right:
                dfs(node.right, cur)

            cur.pop()
        
        dfs(root)
        return ans