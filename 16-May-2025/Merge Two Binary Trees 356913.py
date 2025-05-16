# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        elif not root2:
            return root1
        elif not root1 and not root2:
            return root1

        q1 = deque()
        q1.append(root1)
        q2 = deque()
        q2.append(root2)

        while q2:
            node1 = q1.popleft()
            node2 = q2.popleft()

            node1.val += node2.val

            if node2.left:
                q2.append(node2.left)
                if not node1.left: node1.left = TreeNode()
                q1.append(node1.left)

            if node2.right:
                q2.append(node2.right)
                if not node1.right: node1.right = TreeNode()
                q1.append(node1.right)


        return root1