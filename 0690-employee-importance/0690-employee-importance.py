"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def __init__(self):
        self.importante = 0
        self.visited = set()
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        for employee in employees:
            if employee.id == id:
                self.importante = employee.importance
                break       
        self.dfs(employee,employees)
        return self.importante
    def dfs(self, node, employees):
        self.visited.add(node)
        if not node.subordinates:
            return
        
        for childId in node.subordinates:
            for employee in employees:
                if employee not in self.visited and childId == employee.id:
                    break
            self.importante += employee.importance
            self.dfs(employee,employees)