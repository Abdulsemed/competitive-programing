class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxim  = len(nums)
        exist = [False]*(maxim+1)
        
        for num in nums:
            if 0 < num <= maxim:
                exist[num] = True
                
        for val in range(1, maxim+1):
            if not exist[val]:
                return val
        
        return maxim+1