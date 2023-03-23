class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        left = 0 
        right = len(nums)
        mid = left + (right-left)//2
        leftArr = self.sortArray(nums[left:mid])
        rightArr = self.sortArray(nums[mid:right])
        leftSize = len(leftArr)
        rightSize = len(rightArr)
        left = 0
        right = 0
        arr = []
        while left < leftSize or right < rightSize:
            val1 = leftArr[left] if left < leftSize else float("inf")
            val2 = rightArr[right] if right < rightSize else float("inf")
            if val1 < val2:
                arr.append(val1)
                left += 1
            else:
                arr.append(val2)
                right += 1
        return arr
                
        