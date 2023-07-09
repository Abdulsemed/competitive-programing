class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        nums = sorted(satisfaction, reverse = True)
        index = 0
        while index < len(nums) and nums[index] > -1:
            index += 1
        if index == 0:
            return 0
        sums = 0
        currSum = 0
        for idx in range(index):
            currSum += (nums[idx] *(index-idx))
            sums += nums[idx]
        negatives = []
        idx += 1
        maxim = currSum
        while idx < len(nums):
            negatives.append(nums[idx])
            val = 0
            for index in range(len(negatives)):
                val += (negatives[index] *(len(negatives)-index))
            currSum += sums
            maxim = max(maxim, currSum+val)
            idx += 1
        return maxim