# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        ans = []
        def dfs(node, curSum=0, curNodes=[]):
            if not node: return

            curNodes.append(node.val)
            curSum += node.val

            if not node.left and not node.right:
                if curSum == targetSum:
                    ans.append(curNodes + [])
                return

            dfs(node.left, curSum, curNodes+[])
            dfs(node.right, curSum, curNodes+[])

        dfs(root)
        return ans