class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        size = len(nums)
        for index in range(size):
            if nums[index] % 2 == 0:
                nums[index] = 0
            else:
                nums[index] = 1
        currSum = 0
        count = 0
        dict1 = {0:1}
        for index in range(size):
            currSum += nums[index]
            if currSum - k in dict1:
                count += dict1[currSum-k]
            dict1[currSum] = 1 + dict1.get(currSum,0)
        return count