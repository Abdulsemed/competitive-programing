class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        curr = 1
        left = 0
        right = 0
        count = 0
        if k == 0:
            return 0
        while right < len(nums):
            curr *= nums[right]
            right += 1  
            while left < right and curr >= k:
                curr /= nums[left]
                left += 1
            count += (right-left)
                    
        return count
            