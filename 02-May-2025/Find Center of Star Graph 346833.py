# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution(object):
    def findCenter(self, edges):
        freq = defaultdict(int)

        for x, y in edges:
            freq[x] += 1
            freq[y] += 1

            if freq[x] > 1:
                return x
            if freq[y] > 1:
                return y
        