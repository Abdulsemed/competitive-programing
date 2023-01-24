class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            beg = 0
            end = 1
            while end < len(nums):
                if  nums[end] != 0 and nums[beg]== 0:
                    nums[beg], nums[end] = nums[end], nums[beg]
                    beg += 1
                elif nums[beg] != 0:
                    beg += 1
                end += 1
                    
                
                
        