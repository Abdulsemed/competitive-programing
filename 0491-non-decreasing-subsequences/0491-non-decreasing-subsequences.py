class Solution:
    def __init__(self):
        self.dict = {}
        self.size = 0
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.size = len(nums)
        self.traverse(nums,0,[])
        return self.dict.values()
    def traverse(self,nums,index,path):
        if index >= self.size:
            return
        
        for val in range(index, self.size):
            if not path:
                path.append(nums[val])
                self.traverse(nums,val+1,path[:])
                path.pop()
            elif path[-1] <= nums[val]:
                path.append(nums[val])
                if tuple(path) not in self.dict:
                    self.dict[tuple(path[:])] = path[:]
                self.traverse(nums,val+1,path[:])
                path.pop()