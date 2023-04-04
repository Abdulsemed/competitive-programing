class Solution:
    def __init__(self):
        self.count = 0
        self.maxim = 0
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.maxim = nums[0]
        size = len(nums)
        for index in range(1,size):
            self.maxim = self.maxim | nums[index]
        self.bitwiser(0,0,nums,size)
        return self.count
    def bitwiser(self, index,curr, nums, size):
        if index >= size:
            return 
        for idx in range(index, size):
            prev = curr
            curr = curr|nums[idx]
            if curr == self.maxim:
                self.count += 1
            self.bitwiser(idx+1,curr,nums,size)
            curr = prev
        