class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        size = len(nums)
        stack = sorted(nums)
        if stack == nums:
            return True
        stack = sorted(nums, reverse = True)
        if stack == nums:
            return True
        return False
        