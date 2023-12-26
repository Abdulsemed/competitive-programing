class Solution:
    def __init__(self):
        self.dicts = {}
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    
        def dfs(index,sums,level):
            if level >= n:
                return sums == target
            if (level,sums) in self.dicts:
                return self.dicts[(level, sums)]
            local = 0
            for val in range(1, k+1):
                
                local += dfs(val,sums+val,level+1)
                
            self.dicts[(level,sums)] = local
            return self.dicts[(level,sums)]
        dfs(0,0,0)
        return self.dicts[(0,0)] % (10**9 + 7)
                