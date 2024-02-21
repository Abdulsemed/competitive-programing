class Solution:
    def numSquares(self, n: int) -> int:
        
        def dfs(curr):
            
            if curr == 0:
                return 0
            if curr in dicts:
                return dicts[curr]
            ele = 1
            sqr = 1
            minim = float("inf")
            
            while sqr <= curr:
                minim = min(minim , dfs(curr%sqr) + (curr//sqr))
                ele += 1
                sqr = ele*ele
                
            dicts[curr] = minim
            return dicts[curr]
        dicts = {}
        
        return dfs(n)