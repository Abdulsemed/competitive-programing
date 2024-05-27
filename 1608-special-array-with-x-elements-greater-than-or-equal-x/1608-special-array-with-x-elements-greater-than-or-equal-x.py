class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        def search(index):
            l = 0
            r = len(nums)-1
            while l <= r:
                m = l + (r-l)//2
                
                if nums[m] < index:
                    l = m + 1
                else:
                    r = m -1
            return l
        nums.sort()
        left = 0
        size = len(nums)
        right = nums[-1]
        while left <= right:
            mid = left + (right-left)//2
            pos = search(mid)
            if size - pos  == mid:
                return mid
            elif size - pos > mid:
                left = mid + 1
            else:
                right = mid -1
        return -1