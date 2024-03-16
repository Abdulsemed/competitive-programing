class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxim = -float("inf")
        for element in nums:
            currSum += element
            maxim = max(maxim, currSum)
            if currSum < 0:
                currSum = 0
        
        return maxim