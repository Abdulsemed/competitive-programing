class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        size = len(nums)
        minim = float("inf")
        for index in range(4):
            print(nums[size - 4+index] - nums[index])
            minim = min(minim, nums[size - 4+index] - nums[index])
        
        return minim
        