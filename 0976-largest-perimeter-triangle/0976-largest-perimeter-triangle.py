class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        right = len(nums)-1
        maxPerimeter = 0
        while right > 1:
            side3 = nums[right]
            side2 = nums[right-1]
            side1 = nums[right-2]
            currentPerimeter = side2+side1+side3
            
            if side3 < side1+side2:
                maxPerimeter = max(currentPerimeter, maxPerimeter)
            right -= 1
        
        return maxPerimeter