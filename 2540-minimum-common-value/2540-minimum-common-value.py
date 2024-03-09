class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for element in nums2:
            left = 0
            right = len(nums1)-1
            while left<= right:
                mid = left + (right-left)//2
                if nums1[mid] == element:
                    return element
                elif nums1[mid] < element:
                    left = mid + 1
                else:
                    right = mid -1
        
        return -1
        