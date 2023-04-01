class Solution:
    def __init__(self):
        self.answer = []
        self.visited = 0
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.order(nums,[])
        return self.answer
    
    def order(self,nums,path):
        if len(path) >= len(nums):
            self.answer.append(path)
            return
        for idx in range(len(nums)):
            search = abs(nums[idx])
            if nums[idx] <= 0:
                search += 11
            val = 1<<search
            if  self.visited & val == 0:
                path.append(nums[idx])
                self.visited += 2**search
                self.order(nums,path[:])
                path.pop()
                self.visited -= 2**search
                
        