# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution(object):
    def maximumWealth(self, accounts):
        mx = float('-inf')

        for account in accounts:
            mx = max(mx, sum(account))

        return mx
        