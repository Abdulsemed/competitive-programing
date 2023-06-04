class Solution:
    def __init__(self):
        self.dicts = {}
    def solve(self,index,idx,triangle):
        if index >= len(triangle):
            return 0
        if (index,idx) in self.dicts:
            return self.dicts[(index,idx)]
        count = float("inf")
        self.dicts[(index,idx)] =min(self.solve(index+1,idx,triangle),
                                     self.solve(index+1,idx+1,triangle))+ triangle[index][idx]
        return self.dicts[(index,idx)]
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.solve(0,0,triangle)