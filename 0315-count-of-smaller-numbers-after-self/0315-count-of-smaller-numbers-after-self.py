class Solution:
    def __init__(self):
        self.counts = []
    def countSmaller(self, nums: List[int]) -> List[int]:
        size = len(nums)
        self.counts =[0]*(size)
        for index in range(size):
            nums[index] = (nums[index], index)
        self.mergesort(nums,0,size-1)
        return self.counts
    def mergesort(self,nums,left,right):
        if left == right:
            return [nums[left]]
        mid = left +(right-left)//2
        leftArr = self.mergesort(nums,left,mid)
        rightArr = self.mergesort(nums,mid+1, right)
        
        return self.merger(leftArr,rightArr)
    def merger(self, leftArr, rightArr):
        l_ptr = 0
        r_ptr = 0
        leftSize, rightSize = len(leftArr), len(rightArr)
        while l_ptr < leftSize:
            while r_ptr < rightSize and leftArr[l_ptr][0] <= rightArr[r_ptr][0]:
                r_ptr += 1
            self.counts[leftArr[l_ptr][1]] += rightSize - r_ptr
            l_ptr += 1
        l_ptr, r_ptr = 0,0
        arr = []
        while l_ptr < leftSize or r_ptr < rightSize:
            val1 = leftArr[l_ptr] if l_ptr < leftSize else (-float("inf"),0)
            val2 = rightArr[r_ptr] if r_ptr < rightSize else (-float("inf"),0)
            if val1 > val2:
                arr.append(val1)
                l_ptr += 1
            else:
                arr.append(val2)
                r_ptr += 1
        return arr