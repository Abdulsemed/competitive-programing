class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = 0
        size = len(nums)
        leftSum = 0
        while right < size:
            if leftSum == sum(nums[right+1:]):
                return right
            leftSum += nums[right]
            right += 1
        return -1