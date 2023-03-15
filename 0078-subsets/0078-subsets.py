class Solution:
    def __init__(self):
        self.lists =[[]]
        self.size = 0
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.size = len(nums)
        self.setter(0,nums,[])
        return self.lists
    def setter(self,index, nums,path):
        if index >= self.size:
            return
        
        for j in range(index,self.size):
            path.append(nums[j])
            self.setter(j+1,nums,path[:])
            self.lists.append(path.copy())
            path.pop()
        return