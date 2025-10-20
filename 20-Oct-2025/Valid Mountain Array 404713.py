# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution(object):
    def validMountainArray(self, arr):
        st = []
        flag = False
        if len(arr) < 3: return False
        
        for i in range(len(arr)):
            if not st: st.append(arr[i]); continue

            if arr[i] == st[-1]: return False

            if not flag and st[-1] > arr[i]: 
                if i < 2: return False
                flag = True
            elif flag and st[-1] < arr[i]: return False

            st.append(arr[i])

        return flag
        