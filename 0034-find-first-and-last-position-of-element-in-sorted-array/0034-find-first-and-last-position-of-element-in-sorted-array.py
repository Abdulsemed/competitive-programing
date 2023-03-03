class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        flag = False
        left = 0
        right = len(nums)-1
        odd = -1
        even = -1
        while left <= right:
            mid = left + (right -left)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                flag = True
                break
        if flag:
            while nums[left] != target:
                left += 1
            while nums[right] != target:
                right -= 1
            odd = left
            even = right
        return [odd,even]
                