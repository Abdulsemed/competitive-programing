class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        size = len(nums)
        numDict ={arr[0]:0}
        for index in range(size):
            if arr[index] not in numDict:
                numDict[arr[index]] = index  
        for index in range(size):
            nums[index] = numDict[nums[index]]
        return nums