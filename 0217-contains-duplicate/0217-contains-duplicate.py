class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return sorted(Counter(nums).items(), key=lambda item:item[1], reverse = True)[0][1] > 1