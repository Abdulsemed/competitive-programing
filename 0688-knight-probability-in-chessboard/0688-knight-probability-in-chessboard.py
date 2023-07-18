class Solution:
    def __init__(self):
        self.directions = [(-2,1),(-2,-1),(2,1),(2,-1),(-1,2),(1,2),(-1,-2),(1,-2)]
        self.dicts = defaultdict(int)
        # self.visited = set()
    def inbound(self,row,col,n):
        return 0<= row < n and 0<= col < n
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        return self.dfs(row,column,0,k,n)
    def dfs(self,row,col,level,k,n):
        if level == k:
            return 1
        
        if (row,col,level) in self.dicts:
            return self.dicts[(row,col,level)]
        events = 0
        for _r, _c in self.directions:
            new_r = row+_r
            new_c = col + _c
            if self.inbound(new_r,new_c,n):
                events += self.dfs(new_r,new_c,level+1,k,n)
        self.dicts[(row,col,level)] = events/8
        return self.dicts[(row,col,level)]
            