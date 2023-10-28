class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dicts = {}
        count = 0
        for index in range(len(nums)):
            dicts[nums[index]] = 1 + dicts.get(nums[index],0)
            if index > 0 and nums[index] == nums[index-1] and dicts[nums[index]] > 2:
                idx = index+1
                while idx < len(nums) and nums[index] == nums[idx]:
                    idx += 1
                left = index
                while idx < len(nums):
                    nums[left], nums[idx] = nums[idx],nums[left]
                    left += 1
                    idx += 1
                dicts[nums[index]] = 1 + dicts.get(nums[index],0)
            if index > 0 and (nums[index] < nums[index-1] or dicts[nums[index]] > 2):
                break
            count += 1
        return count
                    