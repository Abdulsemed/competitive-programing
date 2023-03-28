class Solution:
    def __init__(self):
        self.count = 0
    def reversePairs(self, nums: List[int]) -> int:
        self.mergesort(nums,0,len(nums)-1)
        return self.count
    def mergesort(self,arr,left,right):
        if left == right:
            return [arr[left]]
        mid = left + (right-left)//2
        leftArr = self.mergesort(arr,left, mid)
        rightArr = self.mergesort(arr,mid+1, right)
        return self.merger(leftArr,rightArr)
    def merger(self, leftArr, rightArr):
        l_ptr = 0
        r_ptr = 0
        leftSize, rightSize = len(leftArr), len(rightArr)
        while l_ptr < leftSize:
            while r_ptr < rightSize and leftArr[l_ptr] <= rightArr[r_ptr] * 2:
                r_ptr += 1
            self.count += rightSize - r_ptr
            l_ptr += 1
        
        l_ptr, r_ptr = 0 ,0
        arr = []
        while l_ptr < leftSize or r_ptr < rightSize:
            val1 = leftArr[l_ptr] if l_ptr < leftSize else -float("inf")
            val2 = rightArr[r_ptr] if r_ptr < rightSize else -float("inf")
            if val1 > val2:
                arr.append(val1)
                l_ptr += 1
            else:
                arr.append(val2)
                r_ptr += 1
        return arr