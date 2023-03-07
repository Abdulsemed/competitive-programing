class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left <= right:
            mid = left + (right-left)//2
            count = 0
            for element in nums:
                count += math.ceil(element/mid)
            if count <= threshold:
                right = mid - 1
            else:
                left = mid + 1
        return left