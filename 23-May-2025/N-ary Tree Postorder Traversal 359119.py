# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        if not root:
            return []

        res = []

        def dfs(root):
            for x in root.children:
                dfs(x)

            res.append(root.val)
        
        dfs(root)

        return res
        