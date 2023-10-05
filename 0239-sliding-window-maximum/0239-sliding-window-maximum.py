from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        newArr = SortedList()
        for index in range(k):
            newArr.add(nums[index])
          
        left = 0
        right = k-1
        maximArr = [newArr[-1]]
        size = len(nums)
        
        while right+1 < size:
            newArr.remove(nums[left])
            right += 1
            newArr.add(nums[right])
            maximArr.append(newArr[-1])
            left += 1
            
        return maximArr