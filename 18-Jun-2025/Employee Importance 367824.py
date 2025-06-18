# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        def dfs(target):
            idx = 0

            for i in range(len(employees)):
                if employees[i].id == target:
                    idx = i
                    break

            ans = employees[idx].importance

            for i in range(len(employees[idx].subordinates)):
                ans += dfs(employees[idx].subordinates[i])

            return ans

        return dfs(id)