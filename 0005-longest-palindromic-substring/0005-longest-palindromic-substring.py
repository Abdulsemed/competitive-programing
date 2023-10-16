class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        dp = [[0 if row != col else 1 for col in range(len(s))] for row in range(len(s))]
        ans = s[-1]
        for index in range(size-1,-1,-1):
            for val in range(index+1, size):
                if s[index] == s[val] and (dp[index+1][val-1] == 1 or val-index == 1):
                    if len(ans) < val-index+1:
                        ans = s[index:val+1]
                    dp[index][val]= 1
                    
        return ans