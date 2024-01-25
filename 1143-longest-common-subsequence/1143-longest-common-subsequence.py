class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        size1, size2 = len(text1)+1, len(text2)+1
        dp =[[0 for _ in range(size1)] for _ in range(size2)]
        for index in range(1,size2):
            for idx in range(1,size1):
                val = 0
                if index < size2 and idx < size1 and text2[index-1] == text1[idx-1]:
                    dp[index][idx] = max( dp[index][idx], dp[index-1][idx-1] + 1)
                else:
                    dp[index][idx] = max(dp[index][idx], dp[index][idx-1],dp[index-1][idx])
            
        # print(dp)
        return dp[size2-1][size1-1]