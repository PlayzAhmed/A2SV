# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution(object):
    def findRelativeRanks(self, score):
        heap = []
        ans = [0] * len(score)
        prize = {
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal"
        }
        counter = 1

        for i in range(len(score)):
            heappush(heap, (-score[i], i))

        while heap:
            _, i = heappop(heap)

            if counter < 4:
                ans[i] = prize[counter]
            else: 
                ans[i] = str(counter)

            counter += 1

        return ans