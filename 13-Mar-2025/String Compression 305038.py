# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution(object):
    def compress(self, chars):
        count = 1
        n = len(chars)
        last = chars[0]
        temp = []
        res = 0

        if n == 1:
            return 1

        for i in range(1, n):
            if chars[i] == last:
                count += 1
            else:
                res += 1
                if count > 1:
                    res += len(str(count))
                    temp.append(last)
                    temp.extend(list(str(count)))
                    count = 1
                else:
                    temp.append(last)
                last = chars[i]

        if last == chars[n-1]:
            res += 1
            temp.append(last)
            if count > 1:
                temp.extend(list(str(count)))
                res += len(str(count))
        else:
            res += 1
            temp.append(chars[n-1])
        
        chars[:res+1] = temp

        return res