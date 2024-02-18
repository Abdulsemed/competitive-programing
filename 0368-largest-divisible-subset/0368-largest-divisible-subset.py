class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = []
        maxim = 0
        ans = 0
        
        for index in range(len(nums)):
            dp.append([nums[index]])
            
        for index in range(len(nums)-1,-1,-1):
            for val in range(index+1,len(nums)):
                if nums[val] % nums[index] == 0:
                    if len(dp[val]) > len(dp[index])-1:
                        dp[index] = [nums[index]] + dp[val] 
            if len(dp[index]) > maxim:
                maxim = len(dp[index])
                ans = index
                
        return dp[ans]
        