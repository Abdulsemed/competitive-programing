class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for index, elt in enumerate(nums):
            if elt < abs(elt):
                neg.append(elt)
            else:
                pos.append(elt)
        po = 0
        ne = 0
        for index in range(len(nums)):
            if index % 2 == 0:
                nums[index] = pos[po]
                po += 1
            else:
                nums[index] = neg[ne]
                ne += 1
        return nums