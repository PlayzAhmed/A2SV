# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution(object):
    def kClosest(self, points, k):
        # distances = []
        # res = []
        # n = len(points)

        # if n == k:
        #     return points
        
        # for x, y in points:
        #     distance = pow(x, 2) + pow(y, 2)
        #     distances.append(distance)
        #     res.append([x, y])
        #     m = len(distances)
        #     if m > 0:
        #         i = m - 2
        #         while i >= 0 and distance < distances[i]:
        #             distances[i+1] = distances[i]
        #             res[i+1] = res[i]
        #             i -= 1
        #         distances[i+1] = distance
        #         res[i+1] = [x, y]


        # if n / 2 > k:
        #     for i in range(k):
        #         min_index = i
        #         for j in range(i+1, n):
        #             if distances[min_index] > distances[j]:
        #                 min_index = j
        #         distances[min_index], distances[i] = distances[i], distances[min_index]
        #         points[min_index], points[i] = points[i], points[min_index]
        # else:
        #     for i in range(n-1, k-1, -1):
        #         max_index = i
        #         for j in range(i-1, -1, -1):
        #             if distances[max_index] < distances[j]:
        #                 max_index = j
        #         distances[max_index], distances[i] = distances[i], distances[max_index]
        #         points[max_index], points[i] = points[i], points[max_index]

        return sorted(points, key=lambda p: pow(p[0], 2) + pow(p[1], 2))[:k]


        