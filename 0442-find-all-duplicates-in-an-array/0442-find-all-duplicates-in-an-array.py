class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        size = len(nums)
        index = 0
        arr = set()
        while index < size:
            val = nums[index] -1
            if nums[index] == nums[val] and index != val:
                arr.add(nums[index])
                index += 1
            elif index != val:
                nums[index], nums[val] = nums[val], nums[index]
            else:
                index += 1
        return list(arr)