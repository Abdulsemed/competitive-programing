class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicts = {}
        for element in nums:
            dicts[element] = 1 + dicts.get(element,0)
        size = len(nums)/2
        for key in dicts:
            if dicts[key] > size:
                return key
                