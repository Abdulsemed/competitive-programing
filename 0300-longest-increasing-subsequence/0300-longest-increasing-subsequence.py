class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1]*(size)
        for index in range(size-2,-1,-1):
            for val in range(index+1,size):
                if nums[index] < nums[val]:
                    dp[index] = max(dp[index], dp[val]+1)
                                
        return max(dp)