from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        newArr = SortedList()
        for index in range(x,len(nums)):
            newArr.add(nums[index])
            
        minim = float("inf") 
        for index in range(len(nums)-x):
            left = 0
            right = len(newArr)-1
            
            while left<=right:
                mid = left + (right-left)//2
                if newArr[mid] <= nums[index]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            if left < len(newArr):
                minim = min(minim, abs(nums[index]- newArr[left]))
            if left + 1 < len(newArr):
                minim = min(minim, abs(nums[index]- newArr[left+1]))
            if left - 1 > -1:
                minim = min(minim, abs(nums[index]- newArr[left-1]))
            newArr.discard(nums[index+x])
            
        return minim