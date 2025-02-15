# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

import math

class Solution(object):
    def numRabbits(self, answers):
        answers = Counter(answers)
        count = 0

        for k, v in answers.items():
            if k+1 >= v:
                count += k+1
            else:
                g = math.ceil(float(v)/float((k+1)))
                count += (g * (k+1))
                
        return int(count)
        