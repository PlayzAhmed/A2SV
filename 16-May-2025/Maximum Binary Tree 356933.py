# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        root = TreeNode(max(nums))
        index = nums.index(max(nums))
        prefix = nums[:index]
        suffix = nums[index+1:]
        self.inserting(prefix, suffix, root)
        return root
        
    def inserting(self, prefix, suffix, root):
        if prefix:
            new_root = TreeNode(max(prefix))
            index = prefix.index(max(prefix))
            new_prefix = prefix[:index]
            new_suffix = prefix[index+1:]
            root.left = new_root
            self.inserting(new_prefix, new_suffix, new_root)
        if suffix:
            new_root = TreeNode(max(suffix))
            index = suffix.index(max(suffix))
            new_prefix = suffix[:index]
            new_suffix = suffix[index+1:]
            root.right = new_root
            self.inserting(new_prefix, new_suffix, new_root)
        