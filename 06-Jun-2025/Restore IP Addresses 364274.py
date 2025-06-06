# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution(object):
    def restoreIpAddresses(self, s):
        if len(s) > 13:
            return []

        ans = []

        def is_ip(dots):
            temp = ""
            ip = ""
            idx = 0

            for i in range(len(s)):
                if i == dots[idx] and (temp[0] != "0" or len(temp) == 1) and 0 <= int(temp) <= 255:
                    ip += temp 
                    ip += "."
                    temp = ""
                    idx = min(len(dots)-1, idx+1)
                elif i == dots[idx] and not ((temp[0] != "0" or len(temp) == 1) and 0 <= int(temp) <= 255):
                    return False

                temp += s[i]

            if (temp[0] != "0" or len(temp) == 1) and 0 <= int(temp) <= 255 and ip.count(".") == 3:
                ip += temp
                return ip
            return False


        def backtrack(idx=0, dots=[]):
            if len(dots) == 3:
                ip = is_ip(dots)
                if ip:
                    ans.append(ip)
                return
            
            if idx >= len(s):
                return

            for i in range(idx, min(idx+3, len(s))):
                dots.append(i + 1)
                backtrack(i + 1, dots)
                dots.pop()

        backtrack()
        return ans