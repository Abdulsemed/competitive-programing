class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        index = 0
        size = len(nums)
        nums.append(-1)
        size += 1
        while index < size:
            pos = nums[index]
            if nums[index] == -1:
                index += 1
            elif pos != index:
                nums[pos], nums[index] = nums[index], nums[pos]
            else:
                index += 1
        for index in range(size):
            if nums[index] == -1:
                return index