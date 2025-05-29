# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        if not root: return []

        q = deque()
        res = []

        q.append(root)

        while q:
            n = len(q)
            level = [0, 0]
            for i in range(n):
                node = q.popleft()

                level[0] += node.val
                level[1] += 1

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            res.append(float(level[0]) / float(level[1]))

        return res
        