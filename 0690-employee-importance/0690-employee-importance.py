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
        self.visited = set(employees)
        for employee in employees:
            if employee.id == id:
                self.importante = employee.importance
                break       
        self.dfs(employee,employees)
        return self.importante
    def dfs(self, node, employees):
        self.visited.remove(node)
        if not node.subordinates:
            return
        
        for childId in node.subordinates:
            for employee in self.visited:
                if childId == employee.id:
                    break
            self.importante += employee.importance
            self.dfs(employee,employees)