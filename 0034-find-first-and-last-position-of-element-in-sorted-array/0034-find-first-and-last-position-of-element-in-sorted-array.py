class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right -left)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid -1
        odd = left
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right -left)//2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
        even = right
        size =  len(nums)-1
        if not nums or odd > size or even < 0 or nums[odd] != target:
            return [-1, -1]
        return [odd,even]
                