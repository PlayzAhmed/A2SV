# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for x in asteroids:
            if not stack or (stack and x > 0):
                stack.append(x)
            elif x < 0:
                while stack and stack[-1] > 0 and x:
                    if abs(x) > stack[-1]:
                        stack.pop()
                    elif abs(x) == stack[-1]:
                        x = 0
                        stack.pop()
                        break
                    else:
                        x = 0
                        break

                if x:
                    stack.append(x)

        return stack
        