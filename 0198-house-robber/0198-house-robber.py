class Solution:
    def __init__(self):
        self.dicts = {}
    def solve(self,n, nums):
        if n ==0:
            return nums[n]
        if n == 1:
            return max(nums[0], nums[1])
        if n not in self.dicts:
            self.dicts[n] = max(self.solve(n-2,nums)+nums[n], self.solve(n-1, nums))
        return self.dicts[n]
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 3:
            return max(nums)
        return max(self.solve(size-3, nums)+nums[size-1],self.solve(size-2, nums) )
        