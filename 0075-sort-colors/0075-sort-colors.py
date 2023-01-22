class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxim  = max(nums)+1
        numDict = {0:0, 1:0, 2:0}
        for element in nums:
            numDict[element] = 1 + numDict.get(element)
        size = len(nums)
        nums[:] = []
        for index in range(maxim):
            lists = [index]*(numDict[index])
            nums.extend(lists)
        return nums