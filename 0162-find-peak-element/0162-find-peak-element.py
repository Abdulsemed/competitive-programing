class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if mid == 0:
                l = -float("inf")
            else:
                l = nums[mid-1]
            if mid == len(nums)-1:
                r = -float("inf")
            else:
                r = nums[mid+1]
                
            if nums[mid] > r:
                if nums[mid] > l:
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1
                