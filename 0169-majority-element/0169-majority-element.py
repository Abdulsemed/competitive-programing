class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicts = Counter(nums)
        size = len(nums)/2
        for key in dicts:
            if dicts[key] > size:
                return key
                