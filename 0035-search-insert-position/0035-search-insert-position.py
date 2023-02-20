class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index in range(len(nums)):
            if nums[index] == target or nums[index] > target:
                break
        if nums[index] < target:
            index += 1
        return index