# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, temp):
        n = len(temp)
        st = []
        res = [0] * n

        for i in range(n):
            if not st:
                st.append((temp[i], i))
            else:
                while st and st[-1][0] < temp[i]:
                    t, index = st.pop()
                    res[index] = i - index
                st.append((temp[i], i))

        return res

        