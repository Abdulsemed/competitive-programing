class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        index = 0
        while index < size:
            val = nums[index] -1
            if nums[index] == nums[val] and index != val:
                return nums[index]
            elif index != val:
                nums[index], nums[val] = nums[val], nums[index]
            else:
                index += 1
                