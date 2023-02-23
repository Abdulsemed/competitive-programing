class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")
        left = 0
        right = 0
        size = len(nums)
        sumVal = 0
        while right <= size:
            if sumVal >= target:
                minLen = min(minLen, right-left)
                sumVal -= nums[left]
                left += 1
            else:
                if right < size:
                    sumVal += nums[right]
                right += 1
        return minLen if minLen != float("inf") else 0