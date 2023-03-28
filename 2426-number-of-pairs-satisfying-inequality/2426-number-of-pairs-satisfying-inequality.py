class Solution:
    def __init__(self):
        self.count = 0
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        size = len(nums1)
        for index in range(size):
            nums1[index] = nums1[index] - nums2[index]
        self.mergesort(nums1, 0, size-1,diff)
        return self.count
    def mergesort(self, nums,left, right,diff):
        if left == right:
            return [nums[left]]
        mid = left + (right-left)//2
        leftArr = self.mergesort(nums,left,mid,diff)
        rightArr = self.mergesort(nums,mid+1,right,diff)
        
        return self.merger(leftArr,rightArr,diff)
    def merger(self,leftArr,rightArr,diff):
        l_ptr = 0
        r_ptr = 0
        while l_ptr < len(leftArr):
            while r_ptr < len(rightArr) and leftArr[l_ptr] -diff > rightArr[r_ptr] :
                r_ptr += 1
                
            self.count += len(rightArr) - r_ptr
            l_ptr += 1
                
        l_ptr, r_ptr = 0, 0
        arr = []
        while l_ptr < len(leftArr) or r_ptr < len(rightArr):
            val1 = leftArr[l_ptr] if l_ptr < len(leftArr) else float("inf")
            val2 = rightArr[r_ptr] if r_ptr < len(rightArr) else float("inf")
            if val1 < val2:
                arr.append(val1)
                l_ptr += 1
            else:
                arr.append(val2)
                r_ptr += 1
        return arr
        