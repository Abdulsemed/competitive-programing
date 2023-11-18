class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minVal = nums[0]
        minStack = [(nums[0],minVal)]
        size = len(nums)
        for index in range(1,size):
            # print(minStack)
            while minStack and minStack[-1][0] <= nums[index]:
                minStack.pop()
                
            if minStack and nums[index] > minStack[-1][1]:
                return True
            
            minStack.append((nums[index],minVal))
            
            minVal = min(minVal, nums[index])
        return False