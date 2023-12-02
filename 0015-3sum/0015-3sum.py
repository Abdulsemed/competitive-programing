class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        visited = set()
        nums.sort()
        for index in range(len(nums)):
            dicts = {}
            for val in range(index+1,len(nums)):
                if - (nums[val] + nums[index]) in dicts:
                    curr  = tuple(sorted([nums[index], -(nums[index]+nums[val]),nums[val]]))
                    if curr not in visited:
                        answer.append([nums[index],nums[val], - (nums[index]+ nums[val])])
                        visited.add(curr)
                    
                dicts[nums[val]] = 1
                
                        
        return answer