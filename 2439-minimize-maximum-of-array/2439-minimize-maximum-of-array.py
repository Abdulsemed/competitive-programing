class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = nums[0]
        sums = nums[0]
        for index in range(1,len(nums)):
            sums += nums[index]
            result = max(result,math.ceil(sums/(index+1)))
        return result