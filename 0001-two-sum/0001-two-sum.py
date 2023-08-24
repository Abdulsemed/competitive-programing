class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, elt in enumerate(nums):
            if target - elt in hash_map:
                return [hash_map[target-elt], index]
            hash_map[elt] = index
        

