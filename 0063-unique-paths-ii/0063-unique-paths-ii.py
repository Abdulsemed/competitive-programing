class Solution:
    def inbound(self, row, col, rowSize,colSize):
        return 0 <= row < rowSize and 0<= col < colSize
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        directions = [(0,1),(1,0)]
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp =[[0] *(cols) for _ in range(rows)]
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp[-1][-1] = 1
        
        for index in range(rows-1,-1,-1):
            for val in range(cols-1,-1,-1):
                if obstacleGrid[index][val] == 0:
                    for _r, _c in directions:
                        new_r = _r + index
                        new_c = _c + val
                        if self.inbound(new_r,new_c,rows,cols):
                            dp[index][val] += dp[new_r][new_c]
                            
        return dp[0][0]
                    