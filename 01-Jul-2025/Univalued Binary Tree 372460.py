# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        q = deque([root])
        val = root.val

        while q:
            n = len(q)

            for _ in range(n):
                node = q.popleft()

                if node.left:
                    if node.left.val != val: return False
                    q.append(node.left)
                if node.right:
                    if node.right.val != val: return False
                    q.append(node.right)
                    
        return True
                

        