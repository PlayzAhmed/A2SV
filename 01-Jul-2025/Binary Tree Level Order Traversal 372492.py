# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        ans = []
        q = deque([root])

        while q:
            level = []
            n = len(q)

            for _ in range(n):
                node = q.popleft()
                if not node: continue
                
                level.append(node.val)

                q.append(node.left)
                q.append(node.right)

            if level: ans.append(level)

        return ans
        