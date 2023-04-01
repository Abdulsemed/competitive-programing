class Solution:
    def __init__(self):
        self.answer = []
        self.visited = set()
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.order(nums,[])
        return self.answer
    
    def order(self,nums,path):
        if len(path) >= len(nums):
            self.answer.append(path)
            return
        for idx in range(len(nums)):
            if nums[idx] not in self.visited:
                path.append(nums[idx])
                self.visited.add(nums[idx])
                self.order(nums,path[:])
                path.pop()
                self.visited.remove(nums[idx])
                
        