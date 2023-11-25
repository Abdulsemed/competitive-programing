class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs = {}
        count = 0
        size  = len(nums)
        for element in nums:
            goodPairs[element] = 1 + goodPairs.get(element, 0)
            
        for key in goodPairs:
            if goodPairs[key] > 1:
                value = goodPairs[key]
                value = ((value-1)*value)//2
                count += value
        
        return count