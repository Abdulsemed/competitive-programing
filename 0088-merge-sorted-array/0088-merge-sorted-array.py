class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m < 1:
            nums1[:] = nums2
        elif n< 1:
            return 0
        else:
            p1 = m-1
            p2 = n-1
    #         nums1[p1] > nums[p2]
            p3 = m+n-1
            while p3 > 0 and p2 >= 0 and p1 >= 0:
                if nums2[p2] >= nums1[p1]:
                    nums1[p3] = nums2[p2]
                    p2 -= 1
                    p3 -= 1
                else :
                    nums1[p3] = nums1[p1]
                    p3 -= 1
                    p1 -= 1
            if p2 >= 0:
                while p2 >= 0:
                    nums1[p3] = nums2[p2]
                    p3 -= 1
                    p2 -= 1