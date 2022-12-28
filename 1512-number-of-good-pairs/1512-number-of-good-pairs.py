class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs = {}
        count = 0
        size  = len(nums)
        for element in nums:
            goodPairs[element] = 1 + goodPairs.get(element, 0)
            
        for value in goodPairs.values():
            if value > 1:
                value = ((value-1)*value)/2
                count += value
        
        return int(count)