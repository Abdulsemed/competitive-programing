class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        minStack = []
        size= len(nums)
        result = [-1]*(size)
        doubled = (size*2)-1
        for index in range(doubled,-1,-1):
            if minStack and minStack[-1] > nums[index%size]:
                result[index%size] = minStack[-1]
                minStack.append(nums[index%size])
            elif not minStack:
                minStack.append(nums[index%size])
            else:
                while minStack and minStack[-1] <= nums[index%size]:
                    minStack.pop()
                if minStack and minStack[-1] > nums[index%size]:
                    result[index%size] = minStack[-1]
                minStack.append(nums[index%size])
        return result