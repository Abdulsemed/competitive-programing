class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dicts = {}
        indexes = {}
        maxim = 0
        value = 0
        for index,element in enumerate(nums):
            if element not in dicts:
                dicts[element] = 1
                indexes[element] = [index,index]
            else:
                dicts[element] += 1
                indexes[element][1] = index
                
            if dicts[element] > maxim or (dicts[element] == maxim and indexes[element][1] - indexes[element][0] < value):
                value = indexes[element][1] - indexes[element][0]
                maxim = dicts[element]
                
        return value + 1
    
            