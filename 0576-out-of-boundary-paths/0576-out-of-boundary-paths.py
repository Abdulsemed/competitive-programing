class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        dicts = {}
        def dfs(row,col,move):
            if 0> row or row >=m or 0> col or col >=n:
                return 1
            if move < 1:
                return 0
            if(row,col,move) in dicts:
                return dicts[(row,col,move)]
            dicts[(row,col,move)] = 0
            for _r, _c in [(0,1),(1,0),(0,-1),(-1,0)]:
                dicts[(row,col,move)] += dfs(_r+row,_c+col,move-1)
                
            return dicts[(row,col,move)]
        
        return dfs(startRow,startColumn,maxMove) % (10**9+7)