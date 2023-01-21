class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        size = len(nums)
        lists = []
        for index in range(size):
            if nums[index] == target:
                lists.append(index)
        return lists