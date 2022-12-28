class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        size  = len(nums)
        for index, element in enumerate(nums):
            if index + 1 < size:
                right = index + 1
                while right < size:
                    if element == nums[right]:
                        count += 1
                    right += 1
        
        return count