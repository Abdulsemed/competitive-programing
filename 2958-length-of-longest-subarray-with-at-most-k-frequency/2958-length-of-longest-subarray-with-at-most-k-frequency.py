class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxim = 0
        dicts = {}
        left = 0
        right = 0
        while right < len(nums):
            dicts[nums[right]] = 1 + dicts.get(nums[right], 0)
            if dicts[nums[right]] > k:
                while dicts[nums[right]] > k:
                    dicts[nums[left]] -= 1
                    left += 1
            right += 1
            maxim = max(maxim, right-left)
            
        return maxim