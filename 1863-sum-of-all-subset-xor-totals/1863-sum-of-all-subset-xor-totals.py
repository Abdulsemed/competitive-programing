class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        def dfs(index,curr):
            nonlocal ans
            if index >= len(nums):
                return 0
            
            for val in range(index+1,len(nums)):
                
                holder = curr^nums[val]
                dfs(val,holder)
                ans += holder
        for index in range(len(nums)):    
            dfs(index,nums[index])
            ans += nums[index]
        
        return ans