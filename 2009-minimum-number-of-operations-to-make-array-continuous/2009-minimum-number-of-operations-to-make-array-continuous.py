class Solution:
    def minOperations(self, nums: List[int]) -> int:
        oldSize = len(nums)
        nums = list(set(nums))
        nums.sort()
        newSize = len(nums)
        minim = oldSize
        for index in range(newSize):
            bound = (oldSize -1) + nums[index]
            left = index
            right = newSize-1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] <= bound:
                    left = mid + 1
                else:
                    right = mid -1
            minim = min(minim, oldSize-newSize + index + newSize-left)
        
        return minim
            
                    