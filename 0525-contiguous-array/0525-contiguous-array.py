class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dicts = {0:-1}
        currSum = 0
        maxim = 0
        size = len(nums)
        for index in range(size):
            currSum += 1 if nums[index] == 1 else -1
            if currSum in dicts:
                maxim = max(maxim, index - dicts[currSum])
            else:
                dicts[currSum] = index
        return maxim
                