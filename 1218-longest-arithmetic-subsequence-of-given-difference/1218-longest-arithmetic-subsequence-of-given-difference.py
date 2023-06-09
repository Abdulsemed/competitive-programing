class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for element in arr:
            dp[element] = 1 + dp[element - difference]
            
     
        return max(dp.values())