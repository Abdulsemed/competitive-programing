class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        curr = 0
        nums.sort()
        ans = -1
        for index in range(len(nums)):
            if index > 1:
                if curr > nums[index]:
                    ans = curr + nums[index]
            curr += nums[index]
        return ans