class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxim = max(nums)+1
        newArr = [0]*(maxim)
        for element in nums:
            newArr[element] += 1
        val = 0
        for index in range(maxim):
            for _ in range(newArr[index]):
                nums[val] = index
                val+=1
        return nums
        
        