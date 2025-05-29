# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        q = deque()
        q.append(root)
        depth = 0

        while q:
            n = len(q)

            for i in range(n):
                node = q.popleft()
                if node and node.children:
                    for child in node.children:
                        q.append(child)

            depth += 1

        return depth