class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        currSum = 0
        dict1 = {0:1}
        count = 0
        for element in nums:
            currSum += element
            if currSum - goal in dict1:
                count += dict1[currSum-goal]
            dict1[currSum] = 1 + dict1.get(currSum,0)
        return count