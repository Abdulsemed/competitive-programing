class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        negs = 0
        pos = 0
        maxim = -float("inf")
        for index in range(len(nums)-1,-1,-1):
            curr = nums[index] + negs
            negs = min(nums[index], curr,0)
            curr = nums[index] + pos
            pos = max(nums[index],curr,0)
            
            maxim = max(maxim,abs(negs), pos)
            
        return maxim
                