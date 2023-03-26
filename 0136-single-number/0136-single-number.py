class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sorted(Counter(nums).items(), key = lambda item: item[1])[0][0]
        