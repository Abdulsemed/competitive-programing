class Solution:
    def __init__(self):
        self.topK = dict()
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        self.quicksort(nums)
        count = sorted(self.topK.items(), key = lambda item: item[1], reverse =True)
        ans = []
        for element in count:
            if k <= 0: break
            ans.append(element[0])
            k -= 1
            
        return ans
    def quicksort(self, nums):
        size = len(nums)
        if size <= 1:
            if nums and nums[0] not in self.topK:
                self.topK[nums[0]] = 0
            return nums
        
        pivot = size//2
        left, right = [], []
        count = 1
        for index in range(size):
            if index == pivot: 
                continue
            elif nums[index] > nums[pivot]:
                right.append(nums[index])
                continue
            elif nums[index] == nums[pivot]:
                count += 1
            left.append(nums[index])
        if nums[pivot] not in self.topK:
            self.topK[nums[pivot]] = count
            
        leftArr = self.quicksort(left)
        rightArr = self.quicksort(right)
        leftArr.append(nums[pivot])
        leftArr.extend(rightArr)
        return leftArr      
        