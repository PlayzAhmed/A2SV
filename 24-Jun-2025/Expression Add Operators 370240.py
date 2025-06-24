# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution(object):
    def addOperators(self, num, target):
        ans = []

        def back(idx, expression, cur_sum, prev):
            if idx == len(num):
                if cur_sum == target:
                    ans.append(expression)
                return

            for i in range(idx+1, len(num)+1):
                temp_num = num[idx:i]
                if len(temp_num) > 1 and temp_num[0] == "0":
                    return

                cur_val = int(temp_num)
                if idx == 0:
                    back(i, temp_num, cur_val, cur_val)
                else:
                    back(i, expression + "+" + temp_num, cur_sum + cur_val, cur_val)
                    back(i, expression + "-" + temp_num, cur_sum - cur_val, -cur_val)
                    back(i, expression + "*" + temp_num, (cur_sum-prev) + (prev * cur_val), prev * cur_val)
            
        back(0, "", 0, 0)
        return ans