class Solution:
    def minSteps(self, n: int) -> int:
        dp={1:0,2:2}
        if n in dp:
            return dp[n]
        for val in range(3,n+1):
            for index in range(val//2,0,-1):
                if val % index == 0:
                    if index == 1:
                        dp[val] = val
                    else:
                        dp[val] = dp[index] + val//index
                        break
        # print(dp)
        return dp[n]