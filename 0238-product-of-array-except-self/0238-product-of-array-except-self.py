class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        arr = nums.copy()
        for index in range(1,size):
            nums[index] *= nums[index-1]
            arr[size-index-1] *= arr[size-index]
        arr.append(1)
        size += 1
        for index in range(2,size):
            arr[index] = arr[index] * nums[index-2]
        return arr[1:]