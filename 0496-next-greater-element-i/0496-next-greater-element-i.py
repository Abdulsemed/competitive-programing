class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = defaultdict(lambda : -1)
        minStack = [nums2[0]]
        for index in range(1,len(nums2)):
            while minStack and minStack[-1] < nums2[index]:
                val= minStack.pop()
                dict1[val] = nums2[index]
            minStack.append(nums2[index])
        for index in range(len(nums1)):
            nums1[index] = dict1[nums1[index]]
        return nums1