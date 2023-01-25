class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        size = len(nums)
        while right < size:
            
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right] 
                # nums[left+1] = nums[right]
                # left+=2
                # right += 1
        left += 1
        
        return left
        