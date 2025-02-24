# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution(object):
    def robotSim(self, commands, obstacles):
        obstacles = set(map(tuple, obstacles))
        directions = {
            "n": [1, "w", "e"],
            "s": [-1, "e", "w"],
            "e": [1, "n", "s"],
            "w": [-1, "s", "n"],
        }
        current_dir = "n"
        x, y = 0, 0
        max_dis = 0
        
        for c in commands:
            if c > 0:
                if current_dir == "n" or current_dir == "s":
                    for _ in range(c):
                        if (x, y+directions[current_dir][0]) not in obstacles:
                            y += directions[current_dir][0]
                        else:
                            break
                    max_dis = max(max_dis, pow(x, 2)+pow(y, 2))
                else:
                    for _ in range(c):
                        if (x+directions[current_dir][0], y) not in obstacles:
                            x += directions[current_dir][0]
                        else:
                            break
                    max_dis = max(max_dis, pow(x, 2)+pow(y, 2))
            else:
                current_dir = directions[current_dir][c]
                
        
        return max_dis