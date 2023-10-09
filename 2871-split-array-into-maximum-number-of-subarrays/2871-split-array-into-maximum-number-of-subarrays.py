class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        minim = nums[0]
        for index in range(1,len(nums)):
            minim = minim & nums[index]
        
        curr = nums[0]
        tot = 0
        size = 0
        for index in range(len(nums)):
            curr = curr & nums[index]
            if curr + tot <= minim:
                size += 1
                tot += curr
                if index + 1 < len(nums):
                    curr = nums[index+1]
        return size
        
        