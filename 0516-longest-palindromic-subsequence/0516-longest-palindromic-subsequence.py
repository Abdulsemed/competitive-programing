class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for row in range(len(s)):
            for col in range(row,len(s)):
                if s[row] == s[col]:
                    dp[row][col] = 1
        ans = 1
        for row in range(len(s)-2,-1,-1):
            for col in range(row+1,len(s)):
                if s[row] ==s[col]:
                    curr = max(dp[row][col-1] , dp[row+1][col-1] + 2)
                    dp[row][col] = curr
                else:
                    dp[row][col] = max(dp[row][col-1], dp[row+1][col])
                    curr = dp[row][col]
                ans = max(ans, curr)
        # print(dp)
        return ans