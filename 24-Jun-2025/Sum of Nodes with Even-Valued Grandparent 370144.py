# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        ans = [0]
        def dfs(cur, p=None, g=None):
            if not cur: return

            if g and g % 2 == 0: ans[0] += cur.val
            dfs(cur.left, cur.val, p)
            dfs(cur.right, cur.val, p)

        dfs(root)
        return ans[0]

