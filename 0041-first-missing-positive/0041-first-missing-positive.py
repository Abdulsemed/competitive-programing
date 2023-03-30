class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxim  = max(nums)
        size = len(nums)
        ranges = max(maxim,size)
        index = 0
        minim = float("inf")
        for element in nums:
            if element >= 0:
                minim =min(minim,element)
        
        while index < size:
            pos = nums[index] -minim
            if nums[index] < 0 or pos >= size:
                index += 1
            elif index != pos and nums[index] != nums[pos]:
                nums[index], nums[pos] = nums[pos], nums[index]
            else:
                index += 1
        val = 1
        for index in range(size):
            if nums[index] > 0 and (index == 0 or nums[index] >= val):
                if val < nums[index]:
                    return val
                else:
                    val += 1
        return val