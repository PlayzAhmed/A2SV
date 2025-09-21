# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution(object):
    def removeComments(self, source):
        res = []
        in_block = False
        out = ""

        for line in source:
            i = 0
            while i < len(line):
                if not in_block:
                    if i+1 < len(line) and line[i]+line[i+1] == "/*":
                        in_block = True
                        i += 2
                    elif i+1 < len(line) and line[i]+line[i+1] == "//":
                        break
                    else:
                        out += line[i]
                        i += 1
                else:
                    if i+1 < len(line) and line[i]+line[i+1] == "*/":
                        in_block = False
                        i += 2
                    else: 
                        i += 1

            if out and not in_block:
                res.append(out)
                out = ""

        return res

        
