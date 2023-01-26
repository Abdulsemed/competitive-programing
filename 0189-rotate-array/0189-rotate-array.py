class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return 0
        else:
            size = len(nums)
            k = k%size
            result = [0]*(size)
            for index in range(size):
                result[(index+k)%size] = nums[index]
            for index in range(size):
                nums[index] = result[index]
            
        