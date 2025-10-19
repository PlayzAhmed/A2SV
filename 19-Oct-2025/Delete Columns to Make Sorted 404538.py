# Problem: Delete Columns to Make Sorted - https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution(object):
    def minDeletionSize(self, strs):
        ans = 0

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    ans += 1
                    break

        return ans