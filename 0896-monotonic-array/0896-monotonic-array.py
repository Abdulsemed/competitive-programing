class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        size = len(nums)
        stack = []
        if size < 2:
            return True
        flag = None
        for index in range(1,size):
            stack.append(nums[index] - nums[index-1])
            if not flag:
                if stack[-1] < 0:
                    flag = False
                elif stack[-1] > 0:
                    flag = True
        if not flag:
            return True
        for element in stack:
            if flag and element < 0:
                return False
            elif not flag and element > 0:
                return False
        return True
        