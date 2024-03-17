class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        curr = 0
        size = 0
        for index in range(len(groups)):
            size += len(groups[index])
        
        for index in range(len(groups)):
            while curr < len(nums):
                idx = 0
                while curr+idx < len(nums) and groups[index][idx] == nums[curr+idx]:
                    idx += 1
                    if idx == len(groups[index]): break
                if idx == len(groups[index]):
                    if index == len(groups)-1: return True
                    curr += idx
                    break
                curr += 1
            size -= idx
            if len(nums)-curr < size:
                return False
        
        return False
                