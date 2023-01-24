class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return "0"
        nums[:] = list(map(str, nums))
        nums.sort(key = lambda num:num[0], reverse= True)
        size = len(nums)
        for index in range(size):
            temp = index
            for val in range(index+1, size):
                if nums[temp][0] == nums[val][0]:
                    tempSize = len(nums[temp])
                    valSize = len(nums[val])
                    left = 0
                    right = 0
                    while nums[temp][left] == nums[val][right] and (left != tempSize-1 or right != valSize-1):
                        if left+1 < tempSize:
                            left += 1
                        else:
                            left =0
                        if right+1 < valSize:
                            right += 1
                        else:
                            right =0
                    if nums[temp][left] < nums[val][right]:
                        temp = val
                    elif nums[temp][left] == nums[val][right]:
                        if valSize > tempSize:
                            temp = val
                      
                elif nums[temp][0] < nums[val][0]:
                    temp = val
            if temp != index:
                nums[index], nums[temp] = nums[temp], nums[index]
        return ''.join(nums)