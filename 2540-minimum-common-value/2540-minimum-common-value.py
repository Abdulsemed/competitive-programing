class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        sets1 = set(nums1)
        for element in nums2:
            if element in sets1:
                return element
        return -1
        