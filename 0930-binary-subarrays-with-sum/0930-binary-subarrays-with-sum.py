class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        dicts = {0:1}
        currSum = 0
        for element in nums:
            currSum += element
            if currSum - goal in dicts:
                count += dicts[currSum-goal]
            dicts[currSum] = 1 + dicts.get(currSum, 0)
        
        return count