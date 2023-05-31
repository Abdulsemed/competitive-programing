class Solution:
    def fib(self, n: int) -> int:
        dp = [0,1]
        for index in range(2,n+1):
            dp.append(dp[index-1]+dp[index-2])
        return dp[n]
        