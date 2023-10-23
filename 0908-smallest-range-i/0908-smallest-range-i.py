class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxim = max(nums)
        minim = min(nums)
        maxim -= k
        minim += k
        if minim >= maxim:
            return 0
        return maxim - minim