# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution(object):
    def numberOfBoomerangs(self, points):
        counter = 0
        n = len(points)
        
        for i in range(n):
            dis = defaultdict(int)
            for j in range(n):
                if i == j:
                    continue
                
                d = pow((points[i][0]-points[j][0]),2)+pow((points[i][1]-points[j][1]),2)
                dis[d] += 1
            
            for val in dis.values():
                if val > 1:
                    counter += val * (val - 1)
        
        return counter

        