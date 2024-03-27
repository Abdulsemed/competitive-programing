class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        curr = 1
        left = 0
        right = 0
        count = 0
        lastL = 0
        lastR = 0
        if k == 0:
            return 0
        while left < len(nums):
            if curr < k:
                if right < len(nums):
                    curr *= nums[right]
                    right += 1
                    
                else:
                    val = lastR-lastL
                    count -= (val*(val+1))//2
                    val = (right-left)
                    count += (val*(val+1))//2
                    break
            elif left == right:
                right += 1
            else:
                val = lastR-lastL
                count -= (val*(val+1))//2
                val = (right-1-left)
                count += (val*(val+1))//2
                while left < right and curr >= k:
                    curr /= nums[left]
                    left += 1
                lastL = left
                lastR = right-1
                
                    
        return count
            