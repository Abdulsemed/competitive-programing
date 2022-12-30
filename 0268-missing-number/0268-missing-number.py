class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maximum = len(nums)
        Sum = sum(nums)
        expected = (maximum*(maximum+1))//2
        missing = expected - Sum
        return missing
            