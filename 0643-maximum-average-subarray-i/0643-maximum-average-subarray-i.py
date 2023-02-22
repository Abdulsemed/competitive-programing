class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        size = len(nums)
        left = 0
        right = 0
        currSum = nums[right]
        maxSum = -float("inf")
        while right < size:
            if right - left +1 == k:
                maxSum = max(maxSum,currSum)
                currSum -= nums[left]
                left += 1
            right += 1
            if right < size:
                currSum += nums[right]
        return maxSum/k