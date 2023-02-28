class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currSum = 0
        count = 0
        dict1 = {0:1}
        left = 0
        for element in nums:
            currSum += element
            if currSum % k in dict1:
                count += dict1[currSum % k]
            dict1[currSum%k] = 1 + dict1.get(currSum%k, 0)
        return count