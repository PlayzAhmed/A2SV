# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution(object):
    def queryResults(self, limit, queries):
        colors = defaultdict(int)
        balls = defaultdict(int)
        res = []

        for ball, color in queries:
            if balls[ball] and colors[balls[ball]]:
                colors[balls[ball]] -= 1
                if colors[balls[ball]] == 0:
                    colors.pop(balls[ball])

            balls[ball] = color
            colors[color] += 1

            res.append(len(colors))

        return res