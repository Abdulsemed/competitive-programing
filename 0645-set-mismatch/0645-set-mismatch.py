class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        index = 0
        size = len(nums)
        arr = []
        while index < size:
            pos = nums[index]-1
            if nums[index] == nums[pos] and pos != index:
                if nums[index] not in arr:
                    arr.append(nums[index])
                index += 1
            elif pos != index:
                nums[pos], nums[index] = nums[index], nums[pos]
            else:
                index += 1
                
        for index in range(size):
            if nums[index] != index +1:
                arr.append(index+1)
                break
        return arr