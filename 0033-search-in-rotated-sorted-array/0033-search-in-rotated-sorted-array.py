class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = 0
        while left <= right:
            mid = left + (right-left)//2
            if mid + 1 < len(nums) and mid-1 > 0 and nums[mid-1] > nums[mid+1]: break
            if nums[mid] - nums[right] >= 0:
                left = mid + 1
            else:
                right = mid - 1  
        right = mid
        if mid-1 > 0 and nums[mid] - nums[mid-1] < 0:
            right = mid-1
        elif mid +1 < len(nums) and nums[mid] - nums[mid+1] < 0:
            right = mid +1 
        print(right)
        val = self.searcher(nums,target,0,right)
        if val != -1: return val
        left = mid
        
        val = self.searcher(nums,target,right+1 if right+1 < len(nums) else right,len(nums)-1)
        return val
    def searcher(self,nums,target,left,right):
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1