# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution(object):
    def canPartition(self, nums):
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = {0}

        for i in range(len(nums)):
            nxt = set()

            for num in dp:
                if num + nums[i] == target:
                    return True

                nxt.add(num + nums[i])
                nxt.add(num)

            dp = nxt

        return False
        