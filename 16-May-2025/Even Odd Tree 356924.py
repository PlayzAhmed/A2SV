# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        level_index = False
        q = deque()
        q.append(root)

        while q:
            q_len = len(q)
            level_nodes = []
            for _ in range(q_len):
                node = q.popleft()
                if ((not level_index and node.val % 2 == 0) or (level_index and node.val % 2)) or (level_nodes and ((not level_index and node.val <= level_nodes[-1]) or (level_index and node.val >= level_nodes[-1]))):
                    return False
                
                level_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level_index = not level_index
        
        return True