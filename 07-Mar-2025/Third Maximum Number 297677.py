# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution(object):
    def thirdMax(self, nums):
        freq = []

        for num in nums:
            if num not in freq:
                freq.append(num)
        freq.sort(reverse=True)
        return freq[2] if len(freq) >= 3 else max(freq)