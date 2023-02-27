class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict1 = {0:1}
        count = 0
        currSum = 0
        for element in nums:
            currSum += element
            if currSum-k in dict1:
                count += dict1[currSum-k]
            dict1[currSum] = 1 + dict1.get(currSum,0)
        return count