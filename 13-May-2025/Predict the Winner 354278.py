# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution(object):
    def predictTheWinner(self, nums):
        self.nums = nums
        scores = self.game(0, len(nums)-1)
        return scores[0] >= scores[1]

    def game(self, l, r, t=0, s1=0, s2=0):
        if l == r:
            if t == 0: 
                s1 += self.nums[l] 
            else: 
                s2 += self.nums[l]
                
            return [s1, s2]
    
        first = self.game(l+1, r, (t+1) % 2, s1, s2)
        first[t] += self.nums[l]
        second = self.game(l, r-1, (t+1) % 2, s1, s2)
        second[t] += self.nums[r]

        if second[t] > first[t]: return second
        return first