class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1    
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if row == m-1 and col == n-1: continue
                val1 = dp[row][col+1] if col +1  < n else 0 
                val2 = dp[row+1][col] if row +1 < m else 0
                dp[row][col] = val1 + val2       
        return dp[0][0]