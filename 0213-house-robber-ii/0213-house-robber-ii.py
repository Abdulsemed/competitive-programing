class Solution:
    def __init__(self):
        self.dicts = {}
    def solve(self,n, nums,par):
        if n == 0:
            return nums[0]
        if n== 1:
            if par == len(nums)-1:
                return nums[1]
            else:
                return max(nums[1], nums[0])
        
        if (n,par) not in self.dicts:
            if n -2 == (par+1)% len(nums):
                self.dicts[(n,par)] = max(nums[n], self.solve(n-1, nums,par))
            elif n+1 == len(nums):
                self.dicts[(n,par)] = max(self.solve(n-2,nums,n)+nums[n],self.solve(n-1, nums,n-1))
            else:
                self.dicts[(n,par)] = max(self.solve(n-2,nums,par)+nums[n], self.solve(n-1, nums,par))
        return self.dicts[(n,par)]
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 3:
            return max(nums)
        val = self.solve(size-1,nums,size-1)
        return max(val,nums[0])
        