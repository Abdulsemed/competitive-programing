class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = self.quickSort(nums)
        return arr[-k]
    def quickSort(self,nums):
        size = len(nums)
        if size <= 1:
            return nums
        pivot = size//2
        left = []
        right = []
        for index in range(size):
            if index == pivot: continue
            elif nums[index] <= nums[pivot]:
                left.append(nums[index])
            else:
                right.append(nums[index])
        arrLeft = self.quickSort(left)
        arrRight = self.quickSort(right)
        arrLeft.append(nums[pivot])
        arrLeft.extend(arrRight)
        return arrLeft